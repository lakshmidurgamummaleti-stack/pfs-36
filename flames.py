n=input()
m=input() 
l1=[]
l2=[]
n1=""
n2=""
for i in n:
    if i!=" ":
     n1+=i
for i in m:
   if i!=" ":
     n2+=i
 
for i in n1:
   if i in n2:
     l1.append(i)
n=len(l1)
temp=len(n1)+len(n2)-2*n
# print(temp)
# x="flames"
# l=list(x)
# k=0
# while len(l)>1:
#   k=((temp-1+k)%len(l))
#   l.pop(k)
# print(l)

#file handling
def write_file():
    data = input("Enter the text to write: ")
    file = open("sample.txt", "w")
    file.write(data)
    file.close()
    print("Data written successfully.")

def read_file():
    try:
        file = open("sample.txt", "r")
        print("\nFile Contents:")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("File does not exist.")

def append_file():
    data = input("Enter the text to append: ")
    file = open("sample.txt", "a")
    file.write("\n" + data)
    file.close()
    print("Data appended successfully.")

def main():
    while True:
        print("\n----- File Handling Menu -----")
        print("1. Write")
        print("2. Read")
        print("3. Append")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            write_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            append_file()
        elif choice == "4":
            print("Program terminated.")
            break
        else:
            print("Invalid choice! Please try again.")

# Calling the main function
main()