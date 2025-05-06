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

import pyodbc

import FreeCAD

from DraftTools import translate

from MaterialWS.Database.Exceptions import DatabaseConnectionError
from MaterialWS.Configuration import getPreferencesLocation

class Database:

    def __init__(self):
        self._connection = None

        # self._database = "material" # This needs to be generalized

    def _connect(self, noDatabase=False):
        if self._connection is None:
            self._connectODBC(noDatabase)

    def _disconnect(self):
        self._connection = None

    def _cursor(self, noDatabase=False):
        for retry in range(3):
            try:
                self._connect(noDatabase)
                cursor = self._connection.cursor()
                return cursor
            except pyodbc.ProgrammingError:
                # Force a reconnection
                FreeCAD.Console.PrintError(translate('MaterialWS', "\nUnable to connect to database. Reconnecting...\n"))
                self._connection = None

        raise DatabaseConnectionError()

    def _connectODBC(self, noDatabase=False):
        try:
            prefs = getPreferencesLocation()
            connectString = ""
            currentDriver = FreeCAD.ParamGet(prefs).GetString("Driver", "")
            if currentDriver:
                  connectString = connectString + "Driver={%s}" % (currentDriver)
            currentDSN = FreeCAD.ParamGet(prefs).GetString("DSN", "")
            if currentDSN:
                if connectString:
                    connectString = connectString + ';'
                connectString = connectString + 'DSN={}'.format(currentDSN)
            hostname = FreeCAD.ParamGet(prefs).GetString("Hostname", "")
            if hostname:
                if connectString:
                    connectString = connectString + ';'
                connectString = connectString + "Server={}".format(hostname)
            port = FreeCAD.ParamGet(prefs).GetString("Port", "")
            if port:
                  connectString = connectString + ";Port={}".format(port)
            dbName = FreeCAD.ParamGet(prefs).GetString("Database", "material")
            if dbName and not noDatabase:
                  connectString = connectString + ";Database={}".format(dbName)
            username = FreeCAD.ParamGet(prefs).GetString("Username", "")
            if username:
                  connectString = connectString + ";Uid={}".format(username)
            password = FreeCAD.ParamGet(prefs).GetString("Password", "")
            if password:
                  connectString = connectString + ";Pwd={}".format(password)
            connectString = connectString + ";charset=utf8mb4"
            print(connectString)

            self._connection = pyodbc.connect(connectString)
            self._connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
            self._connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
            self._connection.setencoding(encoding='utf-8')
        except Exception as ex:
            print("Unable to create connection:", ex)
            self._connection = None
            raise DatabaseConnectionError(ex)

    def _lastId(self, cursor):
        """Returns the last insertion id"""
        cursor.execute("SELECT @@IDENTITY as id")
        row = cursor.fetchone()
        if row:
            return row.id
        return 0

    def checkCreatePermissions(self):
        return False

    def checkManageUsersPermissions(self):
        return False

    def checkManageLibrariesPermissions(self):
        return False

    def checkCreateLibrariesPermissions(self):
        return False
