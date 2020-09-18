
#numbers=[10,55,30,40,44]
def find_max(numbers):
    max=numbers[0]
    for number in numbers:
        if number>max:
            max=number
    print(max)

#find_max(numbers)