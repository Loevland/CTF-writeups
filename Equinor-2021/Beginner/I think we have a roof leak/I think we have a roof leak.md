Coming Soon!
**I think we have a roof leak.**

> Category: Pwn
>
> The printf function in expects one or more parameters. In the man page its defined as: int printf(const char *format, ...);
> 
> If the first (and only) argument is a pointer string without any formating options it just prints the string. But what happens if we only have one argument, that > is user controlled?
> 
> The man page can be a good place to start.
>
> nc io.ept.gg 30021
