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
Gullible class for use with the GDB gullible plugin.
"""

import signal
import gullible.score

# Build our signal map. This is from stack overvlow. It may have bugs.
# http://stackoverflow.com/questions/2549939/get-signal-names-from-numbers-in-python
signal_map = dict((k, v) for v, k in signal.__dict__.iteritems() if v.startswith('SIG'))

def score(the_gdb):
    "Function to parse the data from gdb and determine what happened"

    gdb_handle = GDB(the_gdb)
    the_score = gullible.score.Score(gdb_handle)
    the_calculator = Calculator(gdb_handle, the_score)
    print the_score.get_cause().name

class GDB:
    "Class to make the python gdb object easier to use"

    def __init__(self, the_gdb):
        self.gdb = the_gdb

    def get_signal(self):
        "Return the signal returned by gdb"

        my_signal = int(self.gdb.parse_and_eval("$_siginfo.si_signo"))
        if signal_map.has_key(my_signal):
            return signal_map[my_signal]
        else:
            return None

class Calculator:
    "Class to process the results of gdb and build the Score object"

    def __init__(self, gdb, score):
        self.gdb = gdb
        self.score = score

        self.__check_signal()

    def __check_signal(self):
        "Check the signal gdb returned"

        signal = self.gdb.get_signal()
        if signal in self.score.scorables:
            self.score.add_item(signal)
