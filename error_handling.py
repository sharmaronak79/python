# try and except are keyword used to hanlde error and avoid programme crashing
# first runt he programme which you write and try diferent posibiities and then check which are the error
# according to that identify the error and use that eror as except key as shown in this programme
#  in this prohgramme when we enter any string value it will throw an eror like ValueError
#so we will use that after except keyword so, it will ignore that and print message whatever we wamt to show
#we can try all posibilities of error and solve it using except  and can pront messgae regarding that
try:
    age=int(input("enter age: "))
    income = 20000
    risk=income/age
    print(f'your age is {age}')
    print(f'your risk is {risk}')
   
except ValueError:
    print('invalid input, try again')
except ZeroDivisionError:
    print('age cannot be zero 0.')