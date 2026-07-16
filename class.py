# class Main():
#     x=30
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def Details(self):
#         print(self.name,self.age,self.marks)
# obj=Main("lakshmi",21,450)
# print(dir(obj))
# obj.Details()

# class Atm():
#     ammount=9999
#     def __init__(self,n,p,balance):
#         self.name=n
#         self.password=p
#         self.b=balance
#     def Details(self):
#         print(self.name,self.password,self.b)
# ac1=Atm("x",1234,9999)
# ac1.b=0
# print(ac1.b)


class Atm():
    ammount=9999
    def __init__(self,n,p,balance):
        self.name=n
        self._p=p
        self.__b=balance
    def Details(self):
        print(self.name,self._p,self.__b)
    def Pin(self,new_pin):
        self._p=new_pin
        print(self._p)
    def Deposit(self,ammount):
        if ammount>0 and ammount%100==0:
            if pin==self._p:
                self._ammount=ammount
                self.__b+=ammount
                print("deposit money",self._ammount)
                print("balance",self.__b)
            else:
                print("enter correct pin")
                
        else:
            print("enter valid ammount")
    def Withdraw(self,ammount):
        if ammount<=0:
        self._ammount=ammount
        self.__b-=ammount
        print("withdraw ammount",self._ammount)
        print("balance",self.__b)
ac1=Atm("x",1234,9999)
ac1.Details()
print(ac1._p)

ac1.Pin(8888)
ac1.Details()
ac1.Deposit(2000)
ac1.Withdraw(1000)
ac1.Deposit(-100)


        