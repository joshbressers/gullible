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

import gullible.gdbwrap
import gullible.score
import gullible.calculator

def crash_analyze(the_gdb):
    "Function to parse the data from gdb and determine what happened"

    gdb_handle = gullible.gdbwrap.GDB(the_gdb)
    the_score = gullible.score.Score(gdb_handle)
    the_calculator = gullible.calculator.Calculator(gdb_handle, the_score)
    print the_score.pretty_print()

