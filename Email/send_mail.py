import smtplib

smtp_objeect = smtplib.SMTP("smtp.gmail.com",587)

smtp_objeect.ehlo()

smtp_objeect.starttls()

import getpass

email = input("enter you E-mail: ")
password = getpass.getpass("Password : ")
smtp_objeect.login(email,password)

from_address = email
to_address = "sharmaronak79@yahoo.com"
subject = input("subject: ")
message = input("Body message : ")
msg = "Subject : "+subject + "\n" + message

smtp_objeect.sendmail(from_address,to_address,msg)

smtp_objeect.quit()
