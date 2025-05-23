# ***************************************************************************
# *   Copyright (c) 2024 David Carter <dcarter@davidcarter.ca>              *
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

import Materials

from MaterialAPI.MaterialManagerExternal import MaterialManagerExternal, \
    MaterialLibraryType, MaterialLibraryObjectType, \
    ModelObjectType, MaterialObjectType

from MaterialWS.WS.WS import WebService
from MaterialWS.WS.Exceptions import WSLibraryCreationError, \
    WSModelCreationError, WSMaterialCreationError, \
    WSModelExistsError, WSMaterialExistsError, \
    WSModelNotFound, WSMaterialNotFound

class MaterialWSManager(MaterialManagerExternal):

    def __init__(self):
        self._ws = WebService()

    def libraries(self) -> list[MaterialLibraryType]:
        # print("libraries()")
        return self._ws.getLibraries()

    def modelLibraries(self) -> list[MaterialLibraryType]:
        # print("modelLibraries()")
        return self._ws.getModelLibraries()

    def materialLibraries(self) -> list[MaterialLibraryType]:
        # print("materialLibraries()")
        return self._ws.getMaterialLibraries()

    def getLibrary(self, name: str) -> MaterialLibraryType:
        print("getLibrary('{}')".format(name))
        return self._ws.getLibrary(name)

    def createLibrary(self, name: str, icon: bytes, readOnly: bool) -> None:
        # print("createLibrary('{}', '{}', '{}')".format(name, icon, readOnly))
        self._ws.createLibrary(name, icon, readOnly)

    def renameLibrary(self, oldName: str, newName: str) -> None:
        print("renameLibrary('{}', '{}')".format(oldName, newName))
        # self._ws.renameLibrary(oldName, newName)

    def changeIcon(self, name: str, icon: bytes) -> None:
        print("changeIcon('{}', '{}')".format(name, icon))
        # self._ws.changeIcon(name, icon)

    def removeLibrary(self, libraryName: str) -> None:
        print("removeLibrary('{}')".format(libraryName))
        # self._ws.removeLibrary(libraryName)

    def libraryModels(self, libraryName: str) -> list[MaterialLibraryObjectType]:
        print("libraryModels('{}')".format(libraryName))
        return self._ws.libraryModels(libraryName)

    def libraryMaterials(self, libraryName: str,
                         filter: Materials.MaterialFilter = None,
                         options: Materials.MaterialFilterOptions = None) -> list[MaterialLibraryObjectType]:
        # print("libraryMaterials('{}')".format(library))
        return self._ws.libraryMaterials(libraryName)
    
    def libraryFolders(self, libraryName: str) -> list[str]:
        print("libraryFolders('{}')".format(libraryName))

    #
    # Model methods
    #

    def getModel(self, uuid: str) -> ModelObjectType:
        print("getModel('{}')".format(uuid))
        return self._ws.getModel(uuid)

    def addModel(self, libraryName: str, path: str, model: Materials.Model) -> None:
        print("addModel('{}', '{}', '{}')".format(libraryName, path, model.Name))
        # self._ws.createModel(libraryName, path, model)

    def migrateModel(self, libraryName: str, path: str, model: Materials.Model) -> None:
        print("migrateModel('{}', '{}', '{}')".format(libraryName, path, model.Name))
        # try:
        #     self._ws.createModel(libraryName, path, model)
        # except WSModelExistsError:
        #     # If it exists we just ignore
        #     pass

    def updateModel(self, libraryName: str, path: str, model: Materials.Model) -> None:
        print("updateModel('{}', '{}', '{}')".format(libraryName, path, model.Name))
        # self._ws.updateModel(libraryName, path, model)

    def setModelPath(self, libraryName: str, path: str, uuid: str) -> None:
        print("setModelPath('{}', '{}', '{}')".format(libraryName, path, uuid))

    def renameModel(self, libraryName: str, name: str,uuid: str) -> None:
        print("renameModel('{}', '{}', '{}')".format(libraryName, name, uuid))

    def moveModel(self, libraryName: str, path: str, uuid: str) -> None:
        print("moveModel('{}', '{}', '{}')".format(libraryName, path, uuid))

    def removeModel(self, uuid: str) -> None:
        print("removeModel('{}')".format(uuid))

    #
    # Material methods
    #

    def getMaterial(self, uuid: str) -> MaterialObjectType:
        print("getMaterial('{}')".format(uuid))
        # return self._ws.getMaterial(uuid)
        raise WSMaterialNotFound()

    def addMaterial(self, libraryName: str, path: str, material: Materials.Material) -> None:
        print("addMaterial('{}', '{}', '{}')".format(libraryName, path, material.Name))
        # self._ws.createMaterial(libraryName, path, material)

    def migrateMaterial(self, libraryName: str, path: str, material: Materials.Material) -> None:
        print("migrateMaterial('{}', '{}', '{}')".format(libraryName, path, material.Name))
        # try:
        #     self._ws.createMaterial(libraryName, path, material)
        # except WSMaterialExistsError:
        #     # If it exists we just ignore
        #     print("Ignore WSModelExistsError error")
        #     pass

    def updateMaterial(self, libraryName: str, path: str, material: Materials.Material) -> None:
        print("updateMaterial('{}', '{}', '{}')".format(libraryName, path, material.Name))

    def setMaterialPath(self, libraryName: str, path: str, uuid: str) -> None:
        print("setMaterialPath('{}', '{}', '{}')".format(libraryName, path, uuid))

    def renameMaterial(self, libraryName: str, name: str, uuid: str) -> None:
        print("renameMaterial('{}', '{}', '{}')".format(libraryName, name, uuid))

    def moveMaterial(self, libraryName: str, path: str, uuid: str) -> None:
        print("moveMaterial('{}', '{}', '{}')".format(libraryName, path, uuid))

    def removeMaterial(self, uuid: str) -> None:
        print("removeMaterial('{}')".format(uuid))
