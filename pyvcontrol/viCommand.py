# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# Copyright 2021 Jochen Schmähling
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
#  Python Module for communication with viControl heatings using the serial Optolink interface
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <http://www.gnu.org/licenses/>.
# ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

from .vi_commands_vitocal200g import VITOCAL200G
import logging

class viCommandException(Exception):
    pass


class viCommand(bytearray):
    """Representation of a command. Object value is a bytearray of address and length."""

    def __init__(
        self,
        command_name: str,
        address: str,
        length: int, 
        unit: str, 
        access_mode: str = None,
        min_value: int = None,
        max_value: int = None
        ):
        """initialize object using the attributes of the chosen command."""

        self.command_name = command_name
        self._command_code = address
        self._value_bytes = length
        self.unit = unit
        self.access_mode = access_mode if access_mode else "read"
        self.vi_data = None

        # create bytearray representation
        b = bytes.fromhex(self._command_code) + self._value_bytes.to_bytes(1, 'big')
        super().__init__(b)

    def __repr__(self):
        return self.command_name

    def response_length(self, access_mode='read'):
        """Returns the number of bytes in the response."""
        # request_response:
        # 2 'address'
        # 1 'Anzahl der Bytes des Wertes'
        # x 'Wert'
        if access_mode.lower() == 'read':
            return 3 + self._value_bytes
        elif access_mode.lower() == 'write':
            # in write mode the written values are not returned
            return 3
        else:
            return 3 + self._value_bytes
