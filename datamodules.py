"""help("modules")#display the all modules"""
'''import math
print(help(math))
print(dir(math))
x=1.23
print(math.ceil(x))
print(math.floor(x))
print(math.sqrt(25))
print(math.remainder(20,120))

print(math.radians(30))#convert the degree to radians
print(math.sin(30))
print(math.sinh(30))
print(math.pow(10,2))
print(math.log(1))
print(math.lcm(10,20,30))
print(math.factorial(5))
print(math.fabs(-12354.33456))# it will change the positive values
'''
# os
"""import os
from os import getcwd,mkdir
print(help(os))
print(os.getcwd())
mkdir("osmodule.py")"""
"""from os import getcwd,mkdir
import os
os.chdir(r"C:\Program Files\Thonny\python.exe")
print("success")
print(os.getcwd())"""

"""import sys
help(sys)
print(sys.getwindowsversion())
print(sys.platform)
print(sys.version)
print(sys.maxsize)
print(sys.path)
print(sys.argv)
print(sys.getsizeof(123456789))"""

def Bharath(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j]<l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
        return(l)
    

#l=[0,1,2,12,17,34]
#Bharath(l)