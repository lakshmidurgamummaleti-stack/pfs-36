"""print((lambda:"this is the new way of function")())"""
"""result=(lambda:"this is the new way of function")
print(result())

print((lambda x:x*x)(10))

result=lambda x:x*x
print(result(10))

print((lambda x,y,z:x if x>y and x>z else y if y>z and y>x else z)(10,20,30))

l=[1,2,3,4,5]
print((lambda l:[i for i in l if i%2==0])(l))"""

"""print((lambda x,y:{x*x,x*y,x-y})(10,20))"""

#map
"""def Str(s):
    x=""
    for i in s:
        x=i.upper()+x#for reverse string using like this x=i+x
    return x

print(Str("mapping"))
print("".join(list(map(Str,"Power"))))"""#for individual letters we can write the remove the join 

"""def Len(l):
    x=[]
    for i in l:
        x.append(len(i))
    return x

l=["java","bava","oracle", "miracle"]
print(Len(l))
print(list(map((lambda x:len(x)),(l))))
result=map((lambda x:len(x)),(l))
print(list(result))

x=[10,25,36,50]
print(list(filter((lambda x:x%2==0),(x))))"""#lambda with filter

"""def Cap(c):
    s=[]
    for i in c:
        s.append(i[0].upper()+i[1:])
    return s

c=["tcs","wipro","capgemini","zoho"]
print(Cap(c))
print(tuple(map((lambda x:x.capitalize()),c)))"""#lambda with map



"""n=["raja","rani","ram","sam","john"]
result=filter((lambda x:x.startswith("r")),n)
print(list(result))"""

"""from functools import reduce
x=[1,2,3,5]
result=reduce((lambda x,y:x+y),x)
print(result)"""


l=[1,2,3]
for i,j in enumerate(l):
    print(i,j)

x=[20,25,3]
y=[10,28,3]
for i in zip(x,y):
    print(i)