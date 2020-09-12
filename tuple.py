# tuples are same as list but it cannot be modified and chnaged, 
# /we can directly assign values using unpacking
#the code is as follow for unpacking, Assume cordinates x,y,z which assigns as follows


print("here now some practise of tuples and unpacking ")
tuple = (10,2,3)
x,y,z=tuple
print(x)
print(y)
print(z)
print("")
print("here now some practise of dictionary : ")
dict = {
    "name": "Ronak",
    "surname" : "Sharma",
    "is varified" : True
}
dict["birthdate"]="9 oct"
print(dict)

print("")

print("practise of mapping of key and assigning value to it : ")
phone=input("Phone: ")
digit_mapping={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five"
}
op=""
for ch in phone:
    op += digit_mapping.get(ch, "x") + " "

print(op)