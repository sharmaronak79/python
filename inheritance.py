#inheritance means to acquire method or function or properties of parent class to other class or child class
# so as shown in example here class father is a parent class
#while creating a second class named mother we write mother(father)
#so, now object of mother class can acquire properties of father class but,
# object of father class cannot use properties of mother class


class father:
    def techer(self):
        print('teaching')
    def farmer(self):
        print('farming')

class mother(father):
    def cook(self):
        print('cooking')

son=mother()
son.cook()
daughter=father()
daughter.techer()
