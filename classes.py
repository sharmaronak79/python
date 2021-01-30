# we  can create a class and add some function  or method to it
# after creating a class whatever method of function create inside will be shwn after use of classe usinf . operator
# during defining any function will use selk as argument as it is called it self
class Detail:  #this is also called template
    def name(self):
        name=input('enter name : ')
        print(f'name is {name}')

    def age(self): #here i have used try and exception also to avoid crashing of programme
        try:
            age=int(input('enter age : '))
            print(f'age is {age}')
        except ValueError:
            print ('invalid input')

#now we will store this created class or template in one object 
# and then we can access its attribute using . operator

student1=Detail()
student1.name()
print('looks good')
student1.age()
student1.standard=10
print(student1.standard)
