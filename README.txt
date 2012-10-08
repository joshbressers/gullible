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
