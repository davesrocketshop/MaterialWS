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
from MaterialAPI.MaterialManagerExternal import MaterialLibraryType, MaterialLibraryObjectType, \
    ModelObjectType, MaterialObjectType

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

    def getLibraries(self) -> list[MaterialLibraryType]:
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

    def getModelLibraries(self) -> list[MaterialLibraryType]:
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

    def getMaterialLibraries(self) -> list[MaterialLibraryType]:
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

    def getLibrary(self, name: str) -> MaterialLibraryType:
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

    def createLibrary(self, name: str, icon: bytes, readOnly: bool) -> None:
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

    def libraryModels(self, libraryName: str) -> list[MaterialLibraryObjectType]:
        models = []
        try:
            response = requests.get(self._baseURL + "libraryModels/{}/".format(libraryName))
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

    def libraryMaterials(self, libraryName: str,
                         filter: Materials.MaterialFilter = None,
                         options: Materials.MaterialFilterOptions = None) -> list[MaterialLibraryObjectType]:
        models = []
        try:
            response = requests.get(self._baseURL + "libraryMaterials/{}/".format(libraryName))
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

    def _getModelProperty(self, property):
        prop = Materials.ModelProperty()
        prop.Name = property["model_property_name"]
        prop.DisplayName = property["model_property_display_name"]
        prop.Type = property["model_property_type"]
        prop.Units = property["model_property_units"]
        prop.URL = property["model_property_url"]
        prop.Description = property["model_property_description"]

        columns = property["columns"]
        for column in columns:
            columnProp = Materials.ModelProperty()
            columnProp.Name = column["model_property_name"]
            columnProp.DisplayName = column["model_property_display_name"]
            columnProp.Type = column["model_property_type"]
            columnProp.Units = column["model_property_units"]
            columnProp.URL = column["model_property_url"]
            columnProp.Description = column["model_property_description"]

            prop.addColumn(columnProp)

        return prop


    def getModel(self, uuid: str) -> ModelObjectType:
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
            inherits = entry["inherits"]
            if len(inherits) > 0:
                model.addInheritance(inherits[0])

            libraryName = entry["library"]

            properties = entry["properties"]
            for property in properties:
                model.addProperty(self._getModelProperty(property))

            return ModelObjectType(libraryName, model)
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise WSConnectionError(error=http_err)
        except Exception as ex:
            print("Unable to get model:", ex)
            raise WSModelNotFound(error=ex)
