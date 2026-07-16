# import re
# text="This is the text i am givivng to tst these regular expressions 1 to 2026 using****"
# result=re.match("This",text)
# print(result)
# print(result.group())
# print(result.span())
# print(result.start())
# print(result.end())
# #search
# r=re.search("these",text)
# print(r)
# print(r.group())
# print(r.span())
# print(r.start())
# #findall
# r=re.findall("these",text)
# print(r)
# #finditer
# iter=list(re.finditer("these",text))
# print(iter)
# for i in re.finditer("these",text):
#      print(i.span())
#      print(i.group())
#      print(i.start())
#      print(i.end())
# replace=re.sub("these","python",text)
# print(replace)
# replace2=re.subn("python","java",replace)
# print(replace2)


# import re
# text="This is the text i am giving to test these regular expressions 1 to 2026 using these *****"
# pattern="[^A-Za-z\d\s]+" #A-Za-z0-9
# result=re.findall(pattern,text)
# print(result)
# print()
# pattern="\d+" #"[0-9]+"
# number=re.findall(pattern,text)
# print(number)
# print()
# pattern="[^\w\s]+" #[0,9]+
# symbols=re.findall(pattern,text)
# print(symbols)
import re
help(re)



# import re
# name="Lakshmi"
# pattern=r"[A-Z][a-z]+"
# if re.fullmatch(pattern,name):
#     print("Valid")
# else:
#     print("Not valid")
#     
# import re
# phone="9345678901"
# # pattern=r"[967][0-9]{9}"
# pattern=r"^\d\d{9}"
# if re.fullmatch(pattern,phone):
# 
#      print("Valid")
# else:
#     print("Not valid")
    
# import re
# aadhar=input()
# pattern=r"\d{12}"
# if re.fullmatch(pattern,aadhar):
#     print("Valid")
# else:
#     print("not valid")
    
# import re
# pan=input()
# patter=r"[A-Z0-9]{10}"
# pattern=r"[A-Z]{5}[0-9]{4}[A-Z]"
# if re.fullmatch(pattern,pan):
#     print("Valid")
# else:
#     print("not valid")


# import re
# email="mld@gmail.com"
#pattern=r"[a-z0-9]+[a-z]+\.com"
# pattern=r"[a-z._]+@gmail.com"
# if re.fullmatch(pattern,email):
#     print("valid")
# else:
#     print("not valid")
    
import re
password="Lakshmi@24"
pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,15}$"
# pattern=r"[A-Za-z0-9$#@*]{8,15}"
if re.fullmatch(pattern,password):
    print("valid")
else:
    print("not valid")