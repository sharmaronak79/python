import smtplib

smtp_objeect = smtplib.SMTP("smtp.gmail.com",587)

smtp_objeect.ehlo()  # this is an extended hello command and also ESMTP protocol, this is sendby email server to itself 

smtp_objeect.starttls()   # TLS provides encryption and security TLS- transport layer security

import getpass  # getpass library is used to keep our password hidden 

email = input("enter your E-mail: ")
password = getpass.getpass("Password : ")  # here w ehave to give our generated app password
smtp_objeect.login(email,password)

from_address = email
to_address = "sharmaronak79@yahoo.com"
subject = input("Subject : ")
message = input("Body Message : ")
msg = "Subject : "+subject + "\n" + message

smtp_objeect.sendmail(from_address,to_address,msg)

smtp_objeect.quit()
