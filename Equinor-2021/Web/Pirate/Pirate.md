**Pirate**

> This one is simple you just need to get the /flag :-)
> 
> Site: Pirate (http://io.ept.gg:30070/)

The site is just a html document with the text:
```
Hello to you
```
But the hint says that we can find the flag in the /flag directory.

We are also given the source code

```python
...
@app.route('/flag', methods=['POST', 'GET'])
def flag():
    return str(key).rstrip()
```
There is also something important in the source code, in another file:
```python
def request(flow):
    if 'flag' in flow.request.url:
        flow.response = http.HTTPResponse.make(403, b"Forbidden, but nice try ;)\n")
```
This forbids us accessing *http://io.ept.gg:30070/flag*, so we must find a way around.

As the python script checks the url for the sub-string "flag" we cannot use that word in the ur.
We can however use the url-encoding of one of the letters in flag to bypass this, 
as the script won't convert the url-encoding to ascii.

The url-encoding for the letter **f** is **%66**, so we pass the url
```
io.ept.gg:30070/%66lag
```
Giving us the webpage with the text:
> EPT{5mugl3r5_liv3_l1k3_k1ng5}
