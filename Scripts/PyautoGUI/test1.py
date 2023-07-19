print("Hello Ronak\nWel COme to the Automation")


#import the relevant modules
import pyautogui
import time

# #Give some delay before continuing the script
# time.sleep(3)

# #Mouse Functions
# print(pyautogui.size())   #print the resolutioon of the screen

# #print the current position of the mouse
# print(pyautogui.position())

#Move the mouse over time(3 seconds)
pyautogui.moveTo(990,-100,5)

pyautogui.moveRel(100,100,3) #move these much of co-ordinates in 3 seconds

#CLICK
pyautogui.click(500,500,3,3,button="Left")
