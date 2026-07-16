# class GrandFather():#single inheritanace
#     def G1(self):
#         print("this is grandparent class")
# 
# 
# class Father(GrandFather):
#     def F1(self):
#         print("this is Father class")
# print(Father.mro())
# obj=Father()
# obj.F1()
# obj.G1()
# g=GrandFather()
# g.G1()



# class GrandFather():#multilevel inheritance
#      def G1(self):
#          print("this is grandparent class")
# 
# class Father(GrandFather):
#      def F1(self):
#          print("this is Father class")
# class Child(Father):
#     def C1(self):
#         print("this is child class")
# c=Child()
# c.C1()
# c.F1()
# c.G1()
# f=Father()
# f.F1()
# 
# 
# class GrandFather():
#     def G1(self):
#         print("this is grandparent class")
#         
# class Father():
#     def F1(self):
#         print("this is Father class")
# class Child(Father,GrandFather):
#     def C1(self):
#         print("this is child class")
# c=Child()
# print(Child.mro())



# class Father():
#     def F1(self):
#         print("this is father class")
# class Child1(Father):
#     def C1(self):
#         print("this is child class")
# class Child2(Father):
#     def C2(self):
#         print("this is child2 class")
# 
# c=Child2()
# c.C2()
# c.F1()
# print(Child1.mro())
# c=Child1()
# c.C1()
# c.F1()
# print(Child2.mro())

class Codegnan():
    def __init__(self,name,address,phno):
        self.name=name
        self.add=address
        self.phno=phno
class Teacher(Codegnan):
    def __init__(self,name,address,phno,bankac,sub):
        super().__init__(name,address,phno)
        self.b=bankac
        self.sub=sub
    def Details(self):
        
        
        print(self.name,self.add,self.phno)
        
class Student(Codegnan):
    def __init__(self,name, address,phno,fphno,cgp):
        super(). __init__(name,address,phno)
    
        self.fphno=fphno
        self.cgp=cgp
    def Details(self):
        print(self.name,self.add,self.phno)
    def OfferCheck(self,ammount=500000):
        if self.cgp>9.5:
            discount=ammount-(ammount*5/100)
            print("discount ammount:",discount)
        else:
            print("No discount")
        
class Developers(Codegnan):
    def __init__(self,name,address,phno,bank_account,qualification):
        super().__init__(name,address,phno)
        self.bank_account
        self.qualification=qualification
    def Details(self):
        print(self.name,self.add,self.phno)
class Helper(Codegnan):
    def __init__(self,name,address,phone,bank_account,work):
        super().__init__(name,address,phno)
        self.bank_account=bank_account
        
        self.work=work
    def Details(self):
        print(self.name,self.add,self.phno)
F1=Teacher("teacher", "xyz",469459884,124738737,"python")
F1.Details()
    
    
    

        
        
        


        