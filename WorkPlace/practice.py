def test():
    print('I am a Test function')
    return True


def play():
    print('I am a play function')
    return int(2)


class Device:
    equip1 = 'Power_Supply'
    equip2 = 'Multi_Meter'

    def __init__(self,n1,n2):
        self.a1 = n1
        self.a2 = n2
        print(f'We have {self.equip1} and {self.equip2}')

    def work(self):
        print('This is init function')
        print(f'I have {self.a1}')
        print(f'I have {self.a2} also')       

######################### Driver Code ###################
from practice import Device
obj = Device("car" , "Jeep")
obj.work()
