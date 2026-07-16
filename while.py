"""for i in range(1,101):
    if i==50:
        break
    if i%5==0:
        continue
    else:
        print(i)
else:
    print("completed")"""

"""for i in range(1,101):
    #if i==50:
       # break
    if i%5==0:
        continue
    else:
        print(i)
else:
    print("completed")"""

"""for i in range(1,101):
    if i%5==0:
        continue
    else:
        print(i)"""


"""n=int(input())
for i in range(10,0,-2):
    print(n,"*",i,"=",n*i)"""
    
"""n=int(input())
for i in range(0,10,-2):
    print(n,"*",i,"=",n*i)"""

"""i=0
while i<=10:
    print(i)
    i+=1"""

"""i=0
while i<=10:
    i+=1
    print(i)"""

"""i=0
while i<=5:
    i+=1
    print(i)
    i+=1"""

"""i=100
while i>=0:
    print(i)
    i-=1"""
"""n=int(input())
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1"""

"""n=int(input())
i=10
while i>=1:
    print(n,"*",i,"=".n*i)
    i-=1"""
"""x=["a","b","e","c","f"]
i=0
while i<len(x):
    print(x[i])
    i+=1"""

"""x=["a","b","e","c","f"]
i=len(x)-1
while i>-1:
    print(x[i])
    i-=1"""

 
"""x=["a","b","e","c","f"]
i=0
while i<len(x):
    if i%2==0:
        print(i)
    i+=1"""

"""x=["a","b","e","c","f"]
l=[]
i=0
while i<len(x):
    if i%2==0:
        #l.append(x[i])
        l+=x[i]
    i+=1
print(l)"""


"""x=["a","b","e","c","d"]
d={}
i=0
while i<len(x):
    print(i)
    print(x[i])
    d[i]=x[i]
    i+=1
print(d)"""


"""x=["a","b","e","c","d"]
d={}
i=0
while i<len(x):
    print(i)
    print(x[i])
    d[i+1]=x[i]
    i+=1
print(d)"""

"""x=["a","b","e","c","d"]
d={}
i=0
while i<len(x):
    print(i)
    print(x[i])
    d[x[i]]=i
    i+=1
print(d)

for k,v in d.items():
    if v%2!=0:
        print(k,v)

x=["a","b","e","c","d"]

keys=[]
values=[]
for k,v in d.items():
    if v%2!=0:
        print(k,v)
        keys.append(k)
        values.append(v)
print(keys,values)
    

di={}
for i in range(len(keys)):
    di[values[i]]=keys[i]
print(di)"""

"""n=int(input())
i=10
while i>=1:
    print(n,"*",i,"=",n*i)
    i-=1"""

