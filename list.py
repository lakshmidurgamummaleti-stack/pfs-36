l=[1,"coder",True,2+3j,12.234]
print(l)

print(l[0],l[3])
print(l[-1])
print(l[0:3])
l.append("lakshmi")
print(l)
l.extend(["lakshmi", "kalyani"])
print(l)
l.append(["lakshmi", "kalyani"])
print(l)
l.insert(1,"vasu")
print(l)
l.remove(1)
print(l)
#l.remove("python")
l.pop(0)
print(l)
x=[1,2,3,4,6]
print(sum(x))
print(min(x))
print(max(x))
print(len(x))

l=[1,2,3,4]
print(id(l))
m=[1,2,3,4]
print(id(m))
