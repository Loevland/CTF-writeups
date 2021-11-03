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

We are given a C-file and an executable. The main function of the c-file looks like this:
```c
int main() {
    ignore_me_init_buffering();
    ignore_me_init_signal();

    char *flagPointer = flag;
    char input[20];
    puts("Enter some text: ");
    fgets(input, 19, stdin);
    printf(input);
    return 0;
}
```
We can the that the *printf* function is missing something (example of printf in the text for the task above).
I came over this writeup for a similar problem (https://nikhilh20.medium.com/format-string-exploit-ccefad8fd66b),
which used the syntax
> %n$s
where n is an integer.

Since this program isn't that big, we can try different numbers from 1 and up.
> %7$s
Gave us the flag
> EPT{w00tw00t_you_found_m3}
