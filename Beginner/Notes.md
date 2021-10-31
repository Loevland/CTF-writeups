**Notes**

> Category: Web
>
> There may be some notes you need to see, or maybe not?
> 
> OWASP can help you if you need some hints, remember this is an old developer.
>
> Site: notes.io.ept.gg

Entering the site we get the same login screen as in *Stonks*.
We know we can log in with 
```
Username: admin
Password: admin
```
We are presented with notes when we are logged in, and we can post them as well.
If we click the note already created, we get the url:
> https://notes.io.ept.gg/note?noteid=2

Weird that we get noteid=2, and not noteid=1 when there is only one note...

The text for the task mention OWASP and an old developer, which means that the site may 
be vulnerable to some attack from the OWASP site.

We can find the top-10 critical security risks on the OWASP site (the different attacks do not differ much for newer version)
https://owasp.org/www-pdf-archive/OWASP_Top_10_-_2013.pdf

Injection is the #1 spot, so we can try to inject in the url of the website.
When viewing the note mentioned previously, we saw that the noteid was 2, we can change the url to:
> https://notes.io.ept.gg/note?noteid=1

And we are presented with:
```
Title:
Admin secret note

Note:
EPT{R3member_2_v3ryf1_us3rs}
```


