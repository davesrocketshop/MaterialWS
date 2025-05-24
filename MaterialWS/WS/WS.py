# ***************************************************************************
# *   Copyright (c) 2025 David Carter <dcarter@davidcarter.ca>              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

__author__ = "David Carter"
__url__ = "https://www.davesrocketshop.com"

import base64

import requests
from requests.exceptions import HTTPError

import Materials
from MaterialAPI.MaterialManagerExternal import MaterialLibraryType, MaterialLibraryObjectType, ModelObjectType

from MaterialWS.WS.Exceptions import WSLibraryCreationError, \
    WSIconError, WSLibraryNotFound, \
    WSModelCreationError, WSMaterialCreationError, \
    WSModelUpdateError, \
    WSModelExistsError, WSMaterialExistsError, \
    WSModelNotFound, WSMaterialNotFound, \
    WSRenameError, WSDeleteError, \
    WSConnectionError

class WebService:
    pass

    def __init__(self):
        self._baseURL = "http://127.0.0.1:8000/materialws/"

    def getLibraries(self):
        libraries = []
        try:
            response = requests.get(self._baseURL + "library")
            response.raise_for_status()

            list = response.json()
            for entry in list:
                print(entry)
                icon = base64.b64decode(entry["library_icon"])
                print("icon:")
                print(icon)
                libraries.append(MaterialLibraryType(entry["library_name"], icon,
                                                     entry["library_read_only"]))
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to get libraries:", ex)
            raise WSLibraryNotFound(error=ex)

        return libraries

    def getModelLibraries(self):
        libraries = []
        try:
            response = requests.get(self._baseURL + "modellibrary")
            response.raise_for_status()

            list = response.json()
            for entry in list:
                print(entry)
                icon = base64.b64decode(entry["library_icon"])
                print("icon:")
                print(icon)
                libraries.append(MaterialLibraryType(entry["library_name"], icon,
                                                     entry["library_read_only"]))
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to get libraries:", ex)
            raise WSLibraryNotFound(error=ex)

        return libraries

    def getMaterialLibraries(self):
        libraries = []
        try:
            response = requests.get(self._baseURL + "materiallibrary")
            response.raise_for_status()

            list = response.json()
            for entry in list:
                print(entry)
                icon = base64.b64decode(entry["library_icon"])
                print("icon:")
                print(icon)
                libraries.append(MaterialLibraryType(entry["library_name"], icon,
                                                     entry["library_read_only"]))
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to get libraries:", ex)
            raise WSLibraryNotFound(error=ex)

        return libraries

    def getLibrary(self, name):
        try:
            response = requests.get(self._baseURL + "library/{}/".format(name))
            response.raise_for_status()

            entry = response.json()
            print(entry)
            icon = base64.b64decode(entry["library_icon"])
            print("icon:")
            print(icon)
            return MaterialLibraryType(entry["library_name"], icon,
                                                    entry["library_read_only"])
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to get library:", ex)
            raise WSLibraryNotFound(error=ex)

    def createLibrary(self, name, icon, readOnly):
        try:
            library = {
                "library_name": name,
                "library_icon": icon,
                "library_read_only": readOnly
            }
            response = requests.post(self._baseURL + "library", json=library)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to create library:", ex)
            raise WSLibraryCreationError(error=ex)

    def libraryModels(self, library):
        models = []
        try:
            response = requests.get(self._baseURL + "libraryModels/{}/".format(library))
            response.raise_for_status()

            list = response.json()
            for entry in list:
                print(entry)
                models.append(MaterialLibraryObjectType(entry["model_id"], entry["library"], entry["folder"]))
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to get library:", ex)
            raise WSLibraryNotFound(error=ex)

        return models

    def libraryMaterials(self, library):
        models = []
        try:
            response = requests.get(self._baseURL + "libraryMaterials/{}/".format(library))
            response.raise_for_status()

            list = response.json()
            for entry in list:
                print(entry)
                models.append(MaterialLibraryObjectType(entry["material_id"], entry["library"], entry["folder"]))
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to get library:", ex)
            raise WSLibraryNotFound(error=ex)

        return models

    def _getModelColumns(self, uuid, propertyName):
        columns = []
        cursor = self._cursor()
        cursor.execute("SELECT model_property_id FROM model_property "
                                    "WHERE model_id = ? AND model_property_name = ?",
                       uuid, propertyName)
        propertyId = 0
        row = cursor.fetchone()
        if row:
            propertyId = row.model_property_id
            cursor.execute("SELECT model_property_name, "
                                    "model_property_display_name, model_property_type, "
                                    "model_property_units, model_property_url, "
                                    "model_property_description FROM model_property_column "
                                    "WHERE model_property_id = ?",
                        propertyId)

            rows = cursor.fetchall()
            for row in rows:
                prop = Materials.ModelProperty()
                prop.Name = row.model_property_name
                prop.DisplayName = row.model_property_display_name
                prop.Type = row.model_property_type
                prop.Units = row.model_property_units
                prop.URL = row.model_property_url
                prop.Description = row.model_property_description

                columns.append(prop)

        return columns

    def _getModelProperties(self, uuid):
        properties = []
        cursor = self._cursor()
        cursor.execute("SELECT model_property_name, "
                                    "model_property_display_name, model_property_type, "
                                    "model_property_units, model_property_url, "
                                    "model_property_description FROM model_property "
                                    "WHERE model_id = ?",
                       uuid)

        rows = cursor.fetchall()
        for row in rows:
            prop = Materials.ModelProperty()
            prop.Name = row.model_property_name
            prop.DisplayName = row.model_property_display_name
            prop.Type = row.model_property_type
            prop.Units = row.model_property_units
            prop.URL = row.model_property_url
            prop.Description = row.model_property_description

            properties.append(prop)

        # This has to happen after the properties are retrieved to prevent nested queries
        for property in properties:
            columns = self._getModelColumns(uuid, property.Name)
            for column in columns:
                property.addColumn(column)

        return properties

    def getModel(self, uuid):
        try:
            response = requests.get(self._baseURL + "model/{}/".format(uuid))
            response.raise_for_status()

            entry = response.json()
            print(entry)
            model = Materials.Model()
            model.Type = entry["model_type"]
            model.Name = entry["model_name"]
            model.URL = entry["model_url"]
            model.Description = entry["model_description"]
            model.DOI = entry["model_doi"]
            model.Directory = entry["folder"]
            model.addInheritance(entry["inherits"])

            libraryName = entry["library"]

            # properties = self._getModelProperties(uuid)
            # for property in properties:
            #     model.addProperty(property)

            return ModelObjectType(libraryName, model)
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to get model:", ex)
            raise WSModelNotFound(error=ex)
