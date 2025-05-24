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
    MaterialLibraryType, MaterialLibraryObjectType

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

    def getLibrary(self, name: str) -> tuple:
        print("getLibrary('{}')".format(name))
        return self._ws.getLibrary(name)

    def createLibrary(self, name: str, icon: str, readOnly: bool) -> None:
        # print("createLibrary('{}', '{}', '{}')".format(name, icon, readOnly))
        self._ws.createLibrary(name, icon, readOnly)

    def renameLibrary(self, oldName: str, newName: str) -> None:
        print("renameLibrary('{}', '{}')".format(oldName, newName))
        # self._ws.renameLibrary(oldName, newName)

    def changeIcon(self, name: str, icon: str) -> None:
        print("changeIcon('{}', '{}')".format(name, icon))
        # self._ws.changeIcon(name, icon)

    def removeLibrary(self, library: str) -> None:
        print("removeLibrary('{}')".format(library))
        # self._ws.removeLibrary(library)

    def libraryModels(self, library: str) -> list[MaterialLibraryObjectType]:
        print("libraryModels('{}')".format(library))
        return self._ws.libraryModels(library)

    def libraryMaterials(self, library: str,
                         filter: Materials.MaterialFilter = None,
                         options: Materials.MaterialFilterOptions = None) -> list[MaterialLibraryObjectType]:
        # import cProfile
        # pr = cProfile.Profile()
        # pr.enable()
        print("libraryMaterials('{}')".format(library))
        mat = self._ws.libraryMaterials(library)

        # pr.disable()
        # pr.dump_stats("/Users/dcarter/Documents/profile.cprof")
        return mat

    def libraryFolders(self, libraryName: str) -> list[str]:
        print("libraryFolders('{}')".format(libraryName))
        # return self._ws.libraryFolders(libraryName)

    #
    # Folder methods
    #

    def createFolder(self, libraryName: str, path: str) -> None:
        print("createFolder('{0}', '{1}')".format(libraryName, path))
        # self._ws.createFolder(libraryName, path)

    def renameFolder(self, libraryName: str, oldPath: str, newPath: str) -> None:
        print("renameFolder('{0}', '{1}', '{2}')".format(libraryName, oldPath, newPath))
        # self._ws.renameFolder(libraryName, oldPath, newPath)

    def deleteRecursive(self, libraryName: str, path: str) -> None:
        print("deleteRecursive('{0}', '{1}')".format(libraryName, path))
        # self._ws.deleteRecursive(libraryName, path)

    #
    # Model methods
    #

    def getModel(self, uuid: str) -> Materials.Model:
        print("getModel('{}')".format(uuid))
        return self._ws.getModel(uuid)

    def addModel(self, library: str, path: str, model: Materials.Model) -> None:
        print("addModel('{}', '{}', '{}')".format(library, path, model.Name))
        # self._ws.createModel(library, path, model)

    def migrateModel(self, library: str, path: str, model: Materials.Model) -> None:
        print("migrateModel('{}', '{}', '{}')".format(library, path, model.Name))
        # try:
        #     self._ws.createModel(library, path, model)
        # except WSModelExistsError:
        #     # If it exists we just ignore
        #     pass

    def updateModel(self, library: str, path: str, model: Materials.Model) -> None:
        print("updateModel('{}', '{}', '{}')".format(library, path, model.Name))
        # self._ws.updateModel(library, path, model)

    def setModelPath(self, library: str, path: str, model: Materials.Model) -> None:
        print("setModelPath('{}', '{}', '{}')".format(library, path, model.Name))

    def renameModel(self, library: str, name: str, model: Materials.Model) -> None:
        print("renameModel('{}', '{}', '{}')".format(library, name, model.Name))

    def moveModel(self, library: str, path: str, model: Materials.Model) -> None:
        print("moveModel('{}', '{}', '{}')".format(library, path, model.Name))

    def removeModel(self, model: Materials.Model) -> None:
        print("removeModel('{}')".format(model.Name))

    #
    # Material methods
    #

    def getMaterial(self, uuid: str) -> Materials.Material:
        print("getMaterial('{}')".format(uuid))
        # return self._ws.getMaterial(uuid)
        raise WSMaterialNotFound()

    def addMaterial(self, library: str, path: str, material: Materials.Material) -> None:
        print("addMaterial('{}', '{}', '{}')".format(library, path, material.Name))
        # self._ws.createMaterial(library, path, material)

    def migrateMaterial(self, library: str, path: str, material: Materials.Material) -> None:
        print("migrateMaterial('{}', '{}', '{}')".format(library, path, material.Name))
        # try:
        #     self._ws.createMaterial(library, path, material)
        # except WSMaterialExistsError:
        #     # If it exists we just ignore
        #     print("Ignore WSModelExistsError error")
        #     pass

    def updateMaterial(self, library: str, path: str, material: Materials.Material) -> None:
        print("updateMaterial('{}', '{}', '{}')".format(library, path, material.Name))

    def setMaterialPath(self, library: str, path: str, material: Materials.Material) -> None:
        print("setMaterialPath('{}', '{}', '{}')".format(library, path, material.Name))

    def renameMaterial(self, library: str, name: str, material: Materials.Material) -> None:
        print("renameMaterial('{}', '{}', '{}')".format(library, name, material.Name))

    def moveMaterial(self, library: str, path: str, material: Materials.Material) -> None:
        print("moveMaterial('{}', '{}', '{}')".format(library, path, material.Name))

    def removeMaterial(self, material: Materials.Material) -> None:
        print("removeMaterial('{}')".format(material.Name))
