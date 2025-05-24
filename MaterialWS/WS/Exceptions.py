# ***************************************************************************
# *   Copyright (c) 2021-2024 David Carter <dcarter@davidcarter.ca>         *
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
"""Class for Web Service exceptions"""

__author__ = "David Carter"
__url__ = "https://www.davesrocketshop.com"

class WSError(Exception):

    def __init__(self, message="Error", error=None):
        self._error = error
        self.message = message

    def __str__(self):
        if self._error is not None:
            return repr(self._error)
        return repr(self.message)

class WSCreationError(WSError):

    def __init__(self, message="Unable to create object", error=None):
        super().__init__(message, error)

class WSTableCreationError(WSError):

    def __init__(self, message="Unable to create table", error=None):
        super().__init__(message, error)

class WSConnectionError(WSError):

    def __init__(self, message="Unable to connect", error=None):
        super().__init__(message, error)

#---
#
# Library errors
#
#---

class WSLibraryCreationError(WSError):

    def __init__(self, message="Unable to create library", error=None):
        super().__init__(message, error)

class WSIconError(WSError):

    def __init__(self, message="Unable to set icon", error=None):
        super().__init__(message, error)

class WSLibraryNotFound(WSError):

    def __init__(self, message="Library not found", error=None):
        super().__init__(message, error)

#---
#
# Model errors
#
#---

class WSModelCreationError(WSError):

    def __init__(self, message="Unable to create model", error=None):
        super().__init__(message, error)

class WSModelUpdateError(WSError):

    def __init__(self, message="Unable to update model", error=None):
        super().__init__(message, error)

class WSModelExistsError(WSError):

    def __init__(self, message="Model exists", error=None):
        super().__init__(message, error)

class WSModelNotFound(WSError):

    def __init__(self, message="Model not found", error=None):
        super().__init__(message, error)

#---
#
# Material errors
#
#---

class WSMaterialCreationError(WSError):

    def __init__(self, message="Unable to create material", error=None):
        super().__init__(message, error)

class WSMaterialExistsError(WSError):

    def __init__(self, message="Material exists", error=None):
        super().__init__(message, error)

class WSMaterialNotFound(WSError):

    def __init__(self, message="Material not found", error=None):
        super().__init__(message, error)

#---
#
# Generic errors
#
#---

class WSRenameError(WSError):

    def __init__(self, message="Unable to rename object", error=None):
        super().__init__(message, error)

class WSDeleteError(WSError):

    def __init__(self, message="Unable to remove object", error=None):
        super().__init__(message, error)
