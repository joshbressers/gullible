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

import gdb
import gullible.gdb

class Gullible(gdb.Command):
    "Analyze a crash to determine exploitability."

    def __init__(self):
        super (Gullible, self).__init__("gullible", gdb.COMMAND_SUPPORT,
                                gdb.COMPLETE_NONE, True)

    def invoke(self, arg, from_tty):
        "Called when the command is invoked from GDB."

        if arg == "debug":
            import pdb; pdb.set_trace()
        gullible.gdb.score(gdb)

Gullible()
