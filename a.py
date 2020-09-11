
numbers=[10,20,30]
print(numbers)
x=input("enter number to append or to add at last of list : ")
x=int(x)
numbers.append(x)
print(numbers)
y= numbers.count(x)
print(f"count of {x} is :{y}")
numbers.sort()
print(f"sorted list in ascending order : {numbers}")
numbers.reverse()
print(f"reverse list in decending order : {numbers}")

