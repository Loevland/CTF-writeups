**Stonks**

> Category: Web
> This is the Stonks System, see if you can get admin access.
> Site: stonks.io.ept.gg

By accessing the site we are presented with a login screen.
We can either create a new account and login with that one, or attempt to
log in with the credentials:

```
Username: admin
Password: admin
```

Which gives us a dashboard page.
When attempting to access the settings page, we are given the message:

> Only admins can view settings

In the cookies of the site we can see:

Name | Value | ... 
--- | --- | ---
Role | EndUser | ...
Session | eyJzdGF0dXMiOiJ1c2VyIn0.YX8UKw.6l8j6V06zVc2bWGFEJZoccd6I3s | ...

We can change the role in the cookie to *Admin*, which gives us access to the settings page,
with the flag: 

> EPT{Cook1es_ar3_fun} 


