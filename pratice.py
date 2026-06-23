"""num=1
for i in range(4):
    for j in range(4):
        print(num,end=" ")
        num+=1
    print()"""
    
"""for i in range(3):
    for j in range(4):
        print(chr(65+j),end=" ")
    print()"""
"""for i in range(5):
    for j in range(3):
        print(chr(97+i),end=" ")
    print()"""

"""for i in range(1,5):
    for j in range(5):
        print(i, end=" ")
        i+=1
    print()"""

"""for i in range(4):
    for j in range(i):
        print(i,end=" ")
    print()"""
"""n=4
for i in range(1,n+1,1):
    for j in range(n-i+1):
        print("*", end=" ")
    print()"""

"""n=5
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or j==0 and i<=n//2 or i==0 and j>=n//2 or j==n-1 and i>=n//2 or i==n-1 and j<=n//2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()"""
o/p
*   * * * 
*   *     
* * * * * 
    *   * 
* * *   * 

"""for i  in range(1,5):
    for j in range(i):
        print(i, end=" ")
    print()"""
        