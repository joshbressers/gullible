# Copyright 2012 Josh Bressers <bressers@redhat.com>
#
# This file is part of gullible.
# 
# gullible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# gullible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with gullible.  If not, see <http://www.gnu.org/licenses/>.

"""
Gullible class for calculating score
"""

class Calculator:
    "Class to process the results of gdb and build the Score object"

    def __init__(self, gdb, score):
        self.gdb = gdb
        self.score = score

        self.__check_signal()
        self.__check_opcode()

    def __check_opcode(self):
        "Check the current instruction"
        instruction = self.gdb.get_instruction()

        for i in self.score.scorables['instructions']:
            if i in instruction:
                self.score.add_item(i)

    def __check_signal(self):
        "Check the signal gdb returned"

        signal = self.gdb.get_signal()
        if signal in self.score.scorables['signals']:
            self.score.add_item(signal)
