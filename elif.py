# tutorial 47
# if elif else statement
# use for multi choices

age= input("enter your age : ")
age = int(age)


if (age==0 or age<0):
    print("enter valid age or you cannot watch the show")

elif 1<age<=5:
    print("ticket prices are $5")
elif 5<age<=20:
    print ("ticket price are $10")
elif 20<age<=50:
    print("tickets price are $20")
elif 50<age<=100:
    print("ticket price are $25")
else:
    print("enter valid age...")