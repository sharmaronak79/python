# tutorial 48
#in key word in if statement

name = input("enter any string : ")
char = input("enter a character that you want to check : ")

if char in name:
    print(" ",char," is available in this given string ",name,"  ")
else:
    print("there is no such ",char," in this string ")    