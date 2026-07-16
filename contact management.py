class Contact:
    def __init__(self):
        self.book={}
class Details(Contact):
    def Create(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
        if name in self.book:
            print("already exists")
        elif phone_no in self.book.values():
            print("number already exists")
        else:
            self.book[self.name]=self.phone_no
            print("success")
        
    def View(self):
        for name,phone  in self.book.items():
            print(f"Name:{name}\tphone:{phone}")
    def Update(self,name,new_name):
        self.name=name
        self.new_name=new_name
        if self.name in self.book and self.new_name not in self.book:
            number=self.book[name]
            self.book[new_name]=number
            print("successfully changed {name} - {new_name}")
        else:
            print(f"{name} or {new_name}already exists")
            
        
obj=Details()
while True:
    n=int(input("1.create \n2.View \n3.update"))
    if n==1:
        name=input("enter the name")
        phone_no=int(input("enter phoneNo:"))
        obj.Create(name,phone_no)
    elif n==2:
        obj.View()
    elif n==3:
        name=input()
        new_name=input()
        
    
        
    
            
        