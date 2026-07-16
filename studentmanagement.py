import os
import random
class Student:
    def Create_file(self,filename):
        if os.path.exists(filename):
            print("already exists")
        else:
            with open(filename, "w") as file:
                file.write(f"Id,Name,Dept,Year,payment\n")
            print("file succefully created")
    def Register(self,name,dept,year,payment,ids=0):
        self.name=name
        self.dept=dept
        self.year=year
        self.payment=payment
        self.ids=ids
        with open("student.csv","a") as file:
            file.write(f"{self.ids},{self.name},{self.dept},{self.year},{self.payment}\n")
        print("file created successfully")
    def view(self):
        Total=0
        members=0
        with open("student.csv","r") as file:
            data=file.readlines()
        for i in data[1:]:
            members+=1
            
            content=i.strip().split(",")
            Total+=float(content[4])
            print(Total)
            print(members)
            
#             print(content[0][:4])
#             print(i)
    def update(self, ids):
        flag = False

    # Read all records
        with open("student.csv", "r") as file:
            data = file.readlines()

    # Rewrite file with updated data
        with open("student.csv", "w") as file:
            file.write(data[0])      # Header

            for record in data[1:]:
                content = record.strip().split(",")

                if content[0] == ids:
                    flag = True

                    print("\nStudent Found")

                    name = input("Enter New Name : ")
                    dept = input("Enter New Department : ")
                    year = input("Enter New Year : ")
                    payment = float(input("Enter New Payment : "))

                    file.write(f"{ids},{name},{dept},{year},{payment}\n")

                    print("\nRecord Updated Successfully!")
                    print("-----------------------------")
                    print("Updated Student Details")
                    print("-----------------------------")
                    print(f"Student ID : {ids}")
                    print(f"Name       : {name}")
                    print(f"Department : {dept}")
                    print(f"Year       : {year}")
                    print(f"Payment    : {payment}")

                else:
                    file.write(record)

        if not flag:
            print("Student ID not found.")
    def pay(self, ids):
        flag = False

        with open("student.csv", "r") as file:
            data = file.readlines()

            for record in data[1:]:
                content = record.strip().split(",")

                if content[0] == ids:
                    flag = True
                    payment = float(input("Enter Payment Amount: "))
                    print("Payment Successful.")
                    break

        if not flag:
            print("Student ID not found.")
            print("Payment Not Allowed.")
    
    def delete(self, ids):
        flag = False

    # Read all records
        with open("student.csv", "r") as file:
            data = file.readlines()

    # Rewrite the file without the deleted record
        with open("student.csv", "w") as file:
            file.write(data[0])      # Header

            for record in data[1:]:
                content = record.strip().split(",")

                if content[0] == ids:
                    flag = True
                    print("\nStudent Found")
                    print("----------------------------")
                    print(f"Student ID : {content[0]}")
                    print(f"Name       : {content[1]}")
                    print(f"Department : {content[2]}")
                    print(f"Year       : {content[3]}")
                    print(f"Payment    : {content[4]}")
                    print("----------------------------")

                    choice = input("Are you sure you want to delete this record? (y/n): ").lower()

                    if choice == "y":
                        print("Record Deleted Successfully.")
                    else:
                        file.write(record)
                        print("Delete Operation Cancelled.")
                else:
                    file.write(record)

        if not flag:
            print("Student ID not found.")
obj=Student()
while True:
    print("1.file\n2.Register\n3.view \n4.update \n5.delete\n6.pay")
    n=int(input("Enter your choice"))
    if n == 1:
        filename=input()
        obj.Create_fil e(filename)
    elif n==2:
        
        name=input()
        dept=input()
        year=input()
        payment=float(input())
        i=" "
        roll=random.sample([1,2,3,4,5,6,7,8,9],k=4)
        for n in roll:
            i+=str(n)
        final=year+i
        ids=final
        obj.Register(name,dept,year,payment,ids)
    elif n==3:
        obj.view()
    elif n==4:
        ids = input("Enter Student ID to Update: ")
        obj.update(ids)
    elif n==5:
         ids = input("Enter Student ID to Delete: ")
         obj.delete(ids)
    elif n==6:
        ids = input("Enter Student ID: ")
        obj.pay(ids)
    else:
        break
        