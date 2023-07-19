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
# pyautogui.moveTo(990,-100,5)

# pyautogui.moveRel(100,100,3) #move these much of co-ordinates in 3 seconds

# #CLICK
# pyautogui.click(500,500,2,3,button="Left")
# # pyautogui.doubleclick()
# # pyautogui.tripleclick()
# # pyautogui.leftclick()

# #SCROLL UP and DOWN
# pyautogui.scroll(-500)
# pyautogui.scroll(500)

#MOUSE UP and DOWN
# pyautogui.mouseUp(100,100,button="left")
# pyautogui.mouseUp(100,100,button="left")


#Example of mouse UP and DOWN
pyautogui.mouseDown(400,400,button="left")
pyautogui.moveTo(800,400,3)
pyautogui.moveTo(400,800,3)
pyautogui.moveTo(400,400,3)
time.sleep(3) #sleep for 3 second
pyautogui.mouseUp()
# pyautogui.moveTo(400,400,3)
# pyautogui.mouseDown(400,400,button="left")
# pyautogui.moveTo(400,800,3)
# pyautogui.mouseUp()
