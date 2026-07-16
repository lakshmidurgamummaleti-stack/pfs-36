
"""import datamodules as d
l=[0,10,3,2,90,1]
print(d.Bharath(l))"""


#random module
import random
help(random)
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10,2))
print(random.choice([1,2,3,54,58]))
print(random.choices([1,2,3,4,5],k=2))
print(random.sample(["a","b","c","d"],k=2))
x=[1,2,3,54,6,87]
random.shuffle(x)
print(x)
