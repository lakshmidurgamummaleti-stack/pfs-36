'''def fun(n):
    list=[]
    for i in range(1,n+1):
        if n%2==0:
            list.append(i)
        elif i%2!=0 and i%5==0:
            list.append("something")
        elif i%2!=0:
            list.append("odd")
    return l
     
n=100
print(fun(n))

print()
print([i if i%2==0 else "something" if i%2!=0 and i%5==0 else "odd" for i in range(1,n+1)])'''


'''def Vowels(l,v):
    for i in 1:
        s=""
        for j in i:
            if j in vowels:
                s+=j
        w.append(j)
    print(w)
l=["rupa","devi","sumanth","john"]
vowels="aeiou"
Vowels(l,vowels)'''

def Fun():
    l=[]
    for i in range(5):
        for j in range(5):
            l.append([i,j])
    return l
print(Fun())

print()#list comprehsions
print([[i,j] for i in range(5) for j in range(5)])