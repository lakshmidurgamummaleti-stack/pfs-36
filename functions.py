"""def Report(name, age, marks):
    print(name, age, marks)
Report("janu",22,453)
Report(456,32,"lakshmi")"""

"""def Details(name,age, marks,institute="codegnan"):
    print(name,age,marks,institute)
    
    
if __name__=="__main__":
    Details("janu",23,456)
    Details(456,32,"kumar")
    Details(marks=456,age=23,name="kumar")
    Details("ram",25,650,"techgnan")"""

"""def Report(name,age,marks):
    print(name,age,marks)
    if age>23 and marks>400:
        print("eligibile")
    else:
        print("not eligibile")
Report("janu",24,456)
Report(marks=456,age=24,name="kumar")"""

"""def Calculator(x,y):
    print(x+y)


Calculator(10,20)"""

"""def Calculator(x,y,z=0):
    print(x+y+z)


Calculator(10,20,30)
Calculator(1,2)
Calculator(1,2,3)"""

"""def Cal(*values):
    print(sum(values))
    
Cal(10,20,3,4,30,40,50,7,8,90)"""

"""def Order(table, *items):
    print(table)
    print(items)
    
Order(2, "chicken_fry", "noodles", "chicken pakoda", "chicken biryani")"""


"""def Order(**items):
    print(items)
    
Order(snack="pizza", topings=1, cheese=2, sauce=4)"""




"""def Report(**args):
    print(args)

Report(h10=1.23,h11=23.22,h12=0.0,h14=34.90)"""

"""def Local(a,b):#local declaration
    print(a,b)

Local(10,20)"""

s=input("enter a string")
reverse_string(s)
print("reversed string:", reverse_string(s))

