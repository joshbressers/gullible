#!/bin/sh

# This will need to be rewritten in a manner that isn't a giant hack.

GULLIBLE_GDB=../gdb/gullible.py

gdb --batch -ex "source $GULLIBLE_GDB" -ex run -ex gullible $1
