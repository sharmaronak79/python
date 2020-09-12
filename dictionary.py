
print("practise of mapping_dictionary of key and assigning value to it  : ")
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
