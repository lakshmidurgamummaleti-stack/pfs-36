# class Car:
#     def Travel(self):
#         print("I am travelling in car")
# class Bike:
#     def Travel(self):
#         print("i am travelling in bike")
# class Train:
#     def Travel(Self):
#         print("this is by train")
#         
# class Walk(Car,Train,Bike):
#     def Travel(self):
#         print("by walk")
# obj=Walk()
# print(Walk.mro())
# obj.Travel()

# class Phonepay:
#     def MoneyTransfer(self):
#         print("money transfer through the phonepe")
# class Googlepay:
#     def MoneyTransfer(self):
#         print("money transfer through the googlepay")
# class creditcard:
#     def MoneyTransfer(self):
#         print("money transfer through the credit card")
# class debitcard:
#     def MoneyTransfer(self):
#         print("money transfer through the debit card")
# obj=Phonepay()
# obj.MoneyTransfer()
# 
# 
# class Calculator:
#     def __init__(self,a,b,c=0,d=0,e=0,f=0):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         self.e=e
#         self.f=f
#     def Add(self):
#         print(self.a+self.b+self.c+self.d+self.e+self.f)
# x=Calculator(10,20)
# x.Add()
# y=Calculator(1,2,3,4,56)
# y.Add()
# 
# #variable length arrugument
# class Calculator:
#     def __init__(self,*Values):
#         self.Values=Values
#     def Add(self):
#         print(self.Values)
#         for i in self.Values:
#             print(i)
# x=Calculator(10,20)
# x.Add()
# y=Calculator(1,2,3,4,5,6)
# y.Add()



# #operating overloading
# class Calculator:
#     def __init__(self,*Values):
#         self.Values=Values
#     def __add__(self):
#         print(sum(self.Values))
# x=Calculator(10,20)
# print(dir(x))
# x.__add__()

#duck typing
class Car:
    def Travel(self):
         print("I am travelling in car")
class Bike:
    def Travel(self):
        print("i am travelling in bike")
class Train:
    def Travel(self):
        print("this is by train")
        
class Walk(Car,Train,Bike):
    def Travel(self):
         print("by walk")
def Calling(obj):
    obj.Travel()
w=Walk(),Train()
for i in w:
    Calling(i)
