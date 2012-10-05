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
import re
import gullible.score

# Build our signal map. This is from stack overvlow. It may have bugs.
# http://stackoverflow.com/questions/2549939/get-signal-names-from-numbers-in-python
signal_map = dict((k, v) for v, k in signal.__dict__.iteritems() if v.startswith('SIG'))

class GDB:
    "Class to make the python gdb object easier to use"

    def __init__(self, the_gdb):
        self.gdb = the_gdb

        # Load our instructions
        the_instructions = self.gdb.execute("disassemble $pc", to_string=True)
        self.instructions = Instructions(the_instructions)

    def get_signal(self):
        "Return the signal returned by gdb"

        my_signal = int(self.gdb.parse_and_eval("$_siginfo.si_signo"))
        if signal_map.has_key(my_signal):
            return signal_map[my_signal]
        else:
            return None

    def get_instruction(self):
        "Return the current instruction mnemonic"

        return self.instructions.get_current_instruction()

class Instructions:
    "Class to store and process the disassembled instructions"

    def __init__(self, instructions):
        self.__raw_instructions = instructions
        self.instructions = []
        self.current = None

        # 0x00000000004004dc <+0>:  push   %rbp
        regex = re.compile('^\s+(0x[0-9a-f]+)\s+(\<\+\d+\>):\s+(.*)$')

        for line in self.__raw_instructions.split("\n"):
            if line.startswith("=>"):
                line = line[2:]
                self.current = len(self.instructions)
            if line and regex.match(line):
                self.instructions.append(regex.match(line).groups())

    def get_current_instruction(self):
        "Return the current instruction"

        return self.instructions[self.current][2]

