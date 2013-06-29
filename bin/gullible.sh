#!/bin/sh

# This will need to be rewritten in a manner that isn't a giant hack.

if [ -z "$GULLIBLE_GDB" ]; then
    GULLIBLE_GDB=../gdb/gullible.py
fi

gdb --batch -ex "source $GULLIBLE_GDB" -ex run -ex gullible $1
