# username and password
# import sys
# import msvcrt

# passwor = ''
# while True:
#     x = msvcrt.getch()
#     if x == '\r':
#         break
#     sys.stdout.write('*')
#     passwor +=x

# print '\n'+pass

username= input ("enter your username: \n")
password = input ("enter your password: \n")

print (" you completed your rwgestration \n welcome to the access world")

user = input ("what is your user name? : \n")
passw = input ("what is your passsword? :\n")

if (username == user and password == passw):
    print ("welcome to next level")
else:
    print ("Incorrect Information")    