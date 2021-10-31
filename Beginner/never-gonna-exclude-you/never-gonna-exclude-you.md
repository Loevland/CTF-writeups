**Never-gonna-exclude-you**

> Category: Crypto
>
> Are we eXclusive, OR?

We are given a txt file with a lot of hexadecimals:
```
25 0c 44 19 45 41 1d 1b 4c 16 0d 00 08 0d 0c 45 13 00 54 18 0a 59 1e 06 ...
```

The name of the task mention xor, so let's try to find the key to xor with (using https://www.dcode.fr/xor-cipher)
Pasting the hexadecimals give us a most likely keylength of 11.

Using the same page we can let the site attempt to brute-force the xor, also giving us the key:
> 7269636b206173746c6579
 
Which in ascii is:
> rick astley

The site does not show all the text with the brute force, as it attempts other solution as well, but 
we can just change the mode to xor with the key we just found.

Giving us:
```
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy
I just wanna tell you how I'm feeling
Gotta make you understand
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
We've known each other for so long
...
RVBUe3gwci0xNS1mdW59
```

At the bottom is some encoding, which turns out to be base64, so we can decrypt it:
```bash
echo "RVBUe3gwci0xNS1mdW59" | base64 -d
```
> EPT{x0r-15-fun}


