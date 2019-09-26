# tutorial 50

# use of loop, while loop

#####################################
# print hello world 10 times 
#
#i = 1

#while i<=10:
 #   print (f"hello world {i}")
  #  i=i+1

###################################

# sum : 1 to 10 or any number

print("sum of 1 to 10 numbers")
i=1
total =0
while i<=10:
    print (f"{total}+{i}={total+i}")
    total = total + i 

    i=i+1
print (f"sum of numbers 1 to 10 = {total}")
print("\n")

print("sum of odd number from 1 to 10")
j=0
k=0
ot=0
while k<10:
    k=j+j+1
    print(f"{ot}+{k}={ot+k}")

    ot = ot + k
    j+=1
print(f"final total sum of odd numbers up to 1 to 10 = {ot}")
print("\n")

print("sum of even number from 1 to 10")
j=1
k=0
et=0
while k<10:
    k=2*j
    print(f"{et}+{k}={et+k}")

    et = et + k
    j+=1
print(f"final total sum of even numbers up to 1 to 10 = {et}")