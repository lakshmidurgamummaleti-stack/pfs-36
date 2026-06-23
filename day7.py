Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={"a":1,"b":2,"c":3}
type(d)
<class 'dict'>
d["c"]
  
SyntaxError: unterminated string literal (detected at line 1)
d["c"]
  
3
d.get("d")
  
print(d.get("d"))
  
None
d.get("c")
  
3
d.keys()
  
dict_keys(['a', 'b', 'c'])
d.values()
  
dict_values([1, 2, 3])
d.items()
  
dict_items([('a', 1), ('b', 2), ('c', 3)])
d
  
{'a': 1, 'b': 2, 'c': 3}
>>> d.update({"d":4})
...   
>>> d
...   
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> d.update({"a":3})
...   
>>> d
...   
{'a': 3, 'b': 2, 'c': 3, 'd': 4}
>>> d.pop("a")
...   
3
>>> d
...   
{'b': 2, 'c': 3, 'd': 4}
>>> d.popitem("d",4)
...   
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d.popitem("d",4)
TypeError: dict.popitem() takes no arguments (2 given)
>>> d.setdefault("d",7)
...   
4
>>> d
...   
{'b': 2, 'c': 3, 'd': 4}
>>> c=d.copy()
...   
>>> c
...   
{'b': 2, 'c': 3, 'd': 4}
>>> c.clear()
...   
>>> c
...   
{}
