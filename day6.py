#tuple
t=(1,2,3,4,"john",2+5j,2.33)
print(t[0:3])
print(len(t))

#set
s=set({False,True,1,2,3,4,5,True,True,2,3,4,5})
print(type(s))
print(s)
#operations
x=set({True,1,2,3})
print(type(x))
print(x)
x.add(8)
print(x)
x.update({4,5,6})
print(x)
x.remove(5)
print(x)
x.pop()
print(x)
x.discard(True)
print(x)
x.clear()
print(x)
#set
dhoni={"vasu", "hari","ram","vignesh","tarun"}
kohli={"pardh","keerthana","preethi","vignesh","tarun"}
print(dhoni.union(kohli))
print(dhoni.intersection(kohli))
print(kohli & dhoni)
print(kohli.difference(dhoni))
print(dhoni-(kohli))
print(kohli.symmetric_difference(dhoni))


x={1,2,3,5,6,4,10}
y={1,2,4,5,6}
print(x.issubset(y))
print(y<=x)
print(x>=y)
print(x.isdisjoint(y))
