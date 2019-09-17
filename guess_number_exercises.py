# tutorial 43
# exercise solution and nested if statement

w_number=27
g_number= input("guess number between 1 to 100 = ")
g_number=int (g_number)
if g_number==w_number:
    print("you win....")
else:
    if g_number>w_number:
        print("your number is too high")
    else: 
        print("your number is too low")
