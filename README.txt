Gullible GDB extension

Gullible is a GDB extension that is designed to help determine if a crash
could be an exploitable security issue.

The name Gullible is a play on words. Microsoft has a tool named
!exploitable. Gullible is a synonym of exploitable in the right context.


Our initial set of testing will use the list Apple included in their
CrashWrangler announcement:

Exploitable if:
        Crash on write instruction
        Crash executing invalid address
        Crash calling an invalid address
        Crash accessing an uninitialized or freed pointer as indicated by
            using the MallocScribble environment variable
        Illegal instruction exception
        Abort due to -fstack-protector, _FORTIFY_SOURCE, heap corruption
            detected
        Stack trace of crashing thread contains certain functions such as
            malloc, free, szone_error, objc_MsgSend, etc.

Not exploitable if:
        Divide by zero exception
        Stack grows too large due to recursion
        Null dereference
        Other abort
        Crash on read instruction


******************************************************************************
How to test

For the moment, gullible isn't really meant to work outside of the
development directory. This will be fixed once we have it working nicely
and are ready to package it.

For now, set your PYTHONPATH to this directory.
% export PYTHONPATH=`pwd`/lib

Change to the bin directory.
% cd bin

Then run the gullible.sh command. For example:

% ./gullible.sh ../tests/testDivideByZero

Program received signal SIGFPE, Arithmetic exception.
0x000000000040054c in main (argc=1, argv=0x7fffffffdeb8) at testDivideByZero.c:9
9       printf("%d\n", 7/0);
DivideByZero


You can run the test suite by running "make test".
