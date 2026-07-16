import os
class Contact:
    def Create_file(self,filename):
        if os.path.exists(filename):
            print("already exists")
        else:
            with open(filename, "w") as file:
                file.write(f"Name,Phone_No\n")
            print("file succefully created")
    def Add_Contact(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
        with open("phonebook.csv","r") as file:
            data=file.readlines()
        with open("phonebook.csv","w") as file :
            flage=False
        for i in data:
            n,p=i.strip().split(",")
            if self.name != n :
                with open("phonebook.csv", "a") as file:
                    file.write(f"{n},{p}\n")
                #print("sucesfully created")
            else:
                with open("phonebook.csv", "a") as file:
                    file.write(f"{n},{p}\n")
                flage=True
        if flage == True:
            print("already exists")
        else:
            with open("phonebook.csv", "a") as file:
                file.write(f"{self.name},{self.phone_no}\n")
            print("added succesfully")
    def update(self,old_name, new_name, new_phone):
        flag=False
        with open("phonebook.csv","r") as file:
            data=file.readlines()
        with open("phonebook.csv","w") as file:
            file.write(data[0]) #header
            for i in data[1:]:
                n,p=i.strip().split(",")
                if n==old_name:
                    file.write(f"{new_name},{new_phone}\n")
                    flag=True
                else:
                    file.write(f"{n},{p}\n")
        if flag:
            print("contact updated")
        else:
            print("already existed")
    def delete(self,name):
        
        
        with open("phonebook.csv","r") as file:
            data=file.readlines()
        flag =False
        with open("phonebook.csv","w") as file:
            file.write(data[0]) #header
            for i in data[1:]:
                n,p=i.strip().split(",")
                if n.strip().lower()==name.strip().lower() :
                    
                    flag=True
                else:
                    file.write(f"{n},{p}\n")
                    
        if flag:
            print("Contact deleted Successfully")
        else:
            print("Contact not found")
                
        
    def View(self):
        file=open("phonebook.csv","r")
        data=file.readlines()
        for details in data:
            name,phone=details.strip().split(",")
            print(f"{name}\t{phone}")

obj=Contact()
while True:
    print("1.Create File\n2.Add_contact\n3.View \n4.Update \n5.Delete")
    n=int(input())
    if n == 1:
        filename=input()
        obj.Create_file(filename)
    elif n == 2:
        name=input()
        phone_no=int(input())
        obj.Add_Contact(name,phone_no)
    elif n == 3:
        obj.View()
    elif n==4:
        old_name=input("enter old name")
        new_name=input("enter new name")
        new_phone=input("Enter phone")
        obj.update(old_name,new_name,new_phone)
    elif n==5:
        name=input("enter deleted name")
        obj.delete(name)
    else:
        break