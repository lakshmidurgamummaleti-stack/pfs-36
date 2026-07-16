# import os
# print(os.getcwd())
# file=open("just.txt",mode="x")
# file.write("hello how are you")
# print("success")
# file.close()

# file=open("just.txt",mode="r")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# data=file.readlines()
# for i in data:
#     print(i)
# file.close()


# file=open("ready","w")
# file.write("this is updated data")
# print("success")
# file.close()

# file=open("ready",mode="a")
# file.write("\njohn and johnson")
# print("success")
# file.close()

# file=open("data.csv","w+")
# file.write("john,127,34")
# print(file.read())
# print("success")
# file.close()


# file=open("info.txt","a")
# name="john"
# age=34;marks=458
# file.write(f"\n{name:<20}{age:}{marks:>15}")
# print("success")
# file.close()

# import smtplib
# from email.mime.text import MIMEText
# server=smtplib.SMTP("smtp.gmail.com",587)
# server.starttls()
# username="lmummaleti@gmail.com"
# password="lans ajmr hvbm jghb"
# server.login(username,password)
# To=["ganginenilakshminagachandrika@gmail.com","shaiksadiya16102005@gmail.com", "deepthikatam18@gmail.com"]
# subject="sending mail"
# message="hello chadrika \n you are a lucky winner 50000 send 1000 to***** number"
# for m in To:
#     msg=MIMEText(message)
#     msg["from"]=username
#     msg["to"]=m
#     msg["subject"]=subject
#     server.sendmail(username,To,msg.as_string())
#     print(f"success sent to {m}")
# server.quit()



# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
# server=smtplib.SMTP("smtp.gmail.com",587)
# server.starttls()
# username="lmummaleti@gmail.com"
# password="lans ajmr hvbm jghb"
# server.login(username,password)
# To="shaiksadiya16102005@gmail.com"
# subject="sending documents using python"
# message=f"Hello {To} i have forwarded the document"
# 
# msg=MIMEMultipart()
# msg["to"]=To
# msg["subject"]=subject
# msg.attach(MIMEText(message))
# filename=r"C:\Users\HP\codegnan_logo.jpg"
# attachement=open(filename,"rb")
# part=MIMEBase("application","octet-stream")
# part.set_payload(attachement.read())
# encoders.encode_base64(part)
# part.add_header("Content-Disposition",f"attachement;filename='{filename}'")
# msg.attach(part)
# server.sendmail(username,To,msg.as_string())
# print("success")
# server.quit()








