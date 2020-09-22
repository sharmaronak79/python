#random is an inbuilt module and/or library which we have to import and then we can access its different 
# method or functions

import random
for i in range(3): #range function for i=0,1,2 so, it iterates through that range
    print(random.randint(10,30))  #randit to enerate random number from that range

team=['ronak','jay','ankit','parth','harsh','hardik']
z=random.choice(team)
print(f'{z} will drive today')
print('')

print('Lets play a Dice game')

class Dice:
    def roll(self):
        first=random.randint(1,6)
        second=random.randint(1,6) 
        return first,second


dice = Dice()
print(dice.roll())