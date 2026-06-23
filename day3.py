Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
bin(10)
'0b1010'
bin(3)
'0b11'
n="11"
print(int(n,2))
3
print(int("1010" , 2))
10
10>>1
5
>>> 10<<1
20
>>> 10<<2
40
>>> 10<<3
80
>>> 37>>3
4
>>> 4
4
>>> oct(7)
'0o7'
>>> oct(18)
'0o22'
>>> oct(98)
'0o142'
>>> oct(15)
'0o17'
>>> oct(13)
'0o15'
>>> print(int("15",8))
13
>>> hex(10)
'0xa'
>>> print(int("a",16))
10
>>> 10
10
>>> hex(26)
'0x1a'
>>> print(int("la",16))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(int("la",16))
ValueError: invalid literal for int() with base 16: 'la'
>>> ~10
-11
>>> ~17
-18
