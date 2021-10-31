**Baby0**

> Category: Reversing
> Magical strings are great.

We are given an executable file baby0
```bash
file baby0
> baby0: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=18f12d481a51a9f8d2e054453bc392beb90d327c, for GNU/Linux 3.2.0, not stripped
```
Let's see if the flag is stored as a string inside the file. 
We know the format starts with EPT, so we can search for that word in the strings.

```bash
strings baby0 | grep EPT
> EPT{strings_are_great!}
```

And we have the flag!
