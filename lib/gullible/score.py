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

"File to facilitate scoring of our crash"

class Score:
    "Class to score our crash"

    scorables = {
        'signals' : [
                        # Signals we care about
                        'SIGSEGV',
                        'SIGABRT',
                        'SIGILL',
                        'SIGFPE'
                    ],

        'instructions' : [
                            # instructions (we just care about the names
                            'div',
                         ]
    }

    def __init__(self, gdb):
        self.gdb = gdb
        self.score = []
        self.__cause = None

    def add_item(self, item):
        "Add a 'score' item to the list"
        self.score.append(item)

    def __check_results(self):
        "Ensure we've parsed the scores"
        if self.__cause is None:
            self.__walk_results()

    def get_cause(self):
        "Return a object representation of the cause"
        self.__check_results()

        return self.__cause

    def __walk_results(self):
        "Walk the result and figure out what happened"

        self.__cause = Unknown()

        # These tests need to cascade from most complex to simplest. The
        # first match wins
        #
        # Long term we want this to work so multiple tests can match, but
        # one may have a better match

        if DivideByZero.score(self.score):
            self.__cause = DivideByZero()
        elif FloatingPoint.score(self.score):
            self.__cause = FloatingPoint()

    def pretty_print(self):
        "Return a nice string explaining the issue"
        self.__check_results()

        return "\n\nDescription: %s\nExploitability: %s\n%s" % \
            (self.__cause.name, self.__cause.exploitable, self.__cause.description)

class Unknown:
    "Class describing an unknown crash, this is the default result."

    def __init__(self):
        self.name = "Unknown"
        self.exploitable = "Unknown"
        self.description = "An unknown crash was detected. It is not known if this issue is dangerous, manual inspection is required."

    @staticmethod
    def score(scores):
        return True

class DivideByZero:
    "Class describing a divide by zero error"

    def __init__(self):
        self.name = "DivideByZero"
        self.exploitable = "NotExploitable"
        self.description = "A divide by zero error has occurred. These are generally not exploitable."

    @staticmethod
    def score(scores):
        "Static method for computing the score for this test."

        if ('SIGFPE' in scores) and ('div' in scores):
            return True
        else:
            return False

class FloatingPoint:
    "Class describing a floating point exception."

    def __init__(self):
        self.name = "FloatingPointException"
        self.exploitable = "Unknown"
        self.description = "A floating point exception has occurred. These are generally not exploitable, but manual verification is needed."

    @staticmethod
    def score(scores):
        "Static method for computing the score for this test."

        if 'SIGFPE' in scores:
            return True
        else:
            return False
