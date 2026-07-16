"""def mcq1():
    count=0
    print("what is the output of 2+3")
    print("A.4\n B.5\n C.2\n D.9\n")
    n=input("enter your choice")
    if n=="B":
        count=count+1
    print("what is the output of the 10-8")
    print("A.5\n B.2\n C.3\n D.5\n")
    n=input("enter your choice")
    if n=="B":
        count=count+1
    print("what is the output of 10%5")
    print("A.0\n B.2\n C.5\n D.6\n")
    n=input("enter your choice")
    if n=="A":
        count=count+1
    print("your score is" , count)
def mcq2():
    count=0

    print("what is the output of 7+3")
    print("A.10\n B.11\n C.12\n D.13\n")
    n=input("enter your choice")
    
    if n=="B":
        count=count+1
    print("what is the output of the 10-8")
    print("A.5\n B.2\n C.3\n D.5\n")
    n=input("enter your choice")
    if n=="B":
        count=count+1
    print("what is the output of 10%5")
    print("A.0\n B.2\n C.5\n D.6\n")
    n=input("enter your choice")
    if n=="A":
        count=count+1
    print("your score is" , count)
print("enter your choice 1.appitude 2.python")
x=int(input())
if x==1:
    mcq2()
else:
    mcq1()"""
#prime number
"""def fun(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    return count
n=int(input())
x=fun(n)
if x==2:
    print("yes")
else:
    print("No")"""
# prime numbers start to end
"""def fun(lower,uppper):
    
    for i in range(lower,upper):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count=count+1
            else:
                continue
            
        if count==2:
            print(i)
lower=int(input())
upper=int(input())

fun(lower,upper)"""

#palindrom
"""def palindrom(n):
    sum=0
    while n>0:

        r=n%10
        sum=sum*10+r
        n=n//10
    print(sum)
n=int(input())
palindrom(n)"""

"""def palindrom(x):
    y=""
    for i in x:
        y=i+y
    print(y)
x=input()
palindrom(x)"""


#anagram
"""def anagram(x,y):
    a=list(x)
    b=list(y)
    a.sort()
    b.sort()
    if a==b:
        print("anagram",a,b)
    else:
        print("not a anagram")
x=input()
y=input()
anagram(x,y)"""
        
    
"""x=input()
y=list(x)#built in
print(y)
arr=[]
for i in x:
    arr.append(i)#not built in
print(arr)"""

#fibonocci
"""def fibonocci(n):
    a=0
    b=1
    for i in range(1,n+1):
        print(a, end="")
        c=a+b
        a=b
        b=c
n=int(input())
fibonocci(n)"""

#factorial
"""def factorial(n):
    fact=1
    while n>0:
        fact=fact*n
        n=n-1
    print(fact)
n=int(input())
factorial(n)"""

#armstrong
"""def armstrong(n):
    sum=0
    a=n
    while a>0:
        r=a%10
        sum=sum+r**3
        a=a//10
    if n==sum:
        print("armstrong")
    else:
        print("not armstrong")
n=int(input())
armstrong(n) """ 
#patterns with numbers
"""n = 4
num = 1

for i in range(1, n + 1):
    for j in range(i):
        if num <= 10:
            print(num, end=" ")
            num += 1
    print()"""
        

"""n=4
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    
    print()"""

"""n=4
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    
    print()"""

"""n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    for j in range(n-i):
        print(" ",end=" ")
    
    print()"""
"""n=5
for i in range(1,5):
    for j in range(n-i):
        print(2*i,end=" ")
    print()"""

"""arr=[1,2,9,5]#user input arr=list(map(int,input().split()))
n=len(arr)
for i in range(n):
    for j in range(n-i):
        print(arr[i],end=" ")
    print()"""
#sum of digits
"""def sum_of_digits(num):
    total=0
    while num>0:
        digit=num%10
        total+=digit
        num//=10
    return total
n=int(input("enter a number"))
print("sum of digits=",sum_of_digits(n))"""

#otp generations
"""import random
def generate_otp():
    otp=random.randint(100000,999999)
    return otp
otp=generate_otp()
print("Your OTP is:",otp)"""
#name pattern
"""x=input("Enter your name to covert into pattern format\n").lower()
n=5
y="love"
z=x.split(" ")
count=0
for i in x:
    
    if i=="a":
        
        print()
        print()
        for i in range(n):
            for j in range(n):
                
                if  (i==0 and j==n//2) or (j==0 and i==n-1) or (j==1 and i ==2) or (i==n//2 and j==n//2) or(j==3 and i ==2) or (j==n-1 and i==n-1):
                    print("*",end=" ")
                    
                else:
                    print(" ",end=" ")
            print()

    elif i=="b":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==0 and j!=n-1) or j==0 or (j==n-1 and (i==1 or i==2 or i==3)) or (i==n-1 and j!=n-1)or i==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="c":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0  or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="d":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==0 and j!=n-1)or j==0 or (j==n-1 and (i==1 or i==2 or i==3)) or (i==n-1 and j!=n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="e":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="f":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="g":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 or i==n-1 or (i==n-2 and j==n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="h":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if   j==0 or i==2 or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="i":
        print()
        print()     
        for i in range(n): 
            for j in range(n):
                if i==0 or i==n-1 or j==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="j":
        print()
        print() 
        for i in range(n):
            for j in range(n): 
                if i==0 or (i==n-1 and (j==0 or j==1)) or j==2:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="k":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if j==0 or (i==1 and j==2) or (i==0 and j==3) or (i==2 and j==1) or (i==4 and j==3) or (i==3 and j==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    
    elif i=="l":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if j==0 or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="m":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if j==0 or (i==1 and (j==1 or j==3)) or j==n-1 or (i==2 and j==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="n":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if j==0 or i==j or j==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="o":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or j==n-1 or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="p":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 or (i==1 and j==n-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="q":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==n-1 or i==2 or( j==0 and i==1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="r":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==0 or i==2 or j==n-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="s":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or (i==1 and j==0) or i==2 or (i==n-2 and j==n-1) or i==n-1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="t":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or j==n//2 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="u":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==n-1 or j==0 or j==n-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="v":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==0 and j==0)or (i==2 and j==1) or (j==n//2 and i==(n-1)) or (i==0 and j==n-1) or (i==2 and j ==n-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="w":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==n//2 and j==n//2) or j==0 or j==n-1 or (i==n-2 and(j==1 or j==n-2)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="x":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==j or i==(n-j-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="y":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if (i==0 and j==0) or (i==1 and j==1)or i==(n-j-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i=="z":
        print()
        print()
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1 or i==(n-j-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    elif i==" ":
        print()
        print()
        
        for i in z:
            if i=="love":
                r=5
                c=7
                
                while count<=0: 
                    for i in range(r):
                        for j in range(c):
                            if (i==0 and j%3!=0) or (i==1 and j%3==0) or j==(c-i) or (i==j+1):
                                print("*",end=" ")
                            else:
                                print(" ",end=" ")
                        print()
                        count+=1
                        continue
                        
                else:
                    print()
    
    else:
        print(" Enter Alphabets Only")"""

n="john"
for i in range(1,len(n)+1):
    print(n[i:]+n[:i])