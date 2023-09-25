#This is for test equipment for the Lab

import pyvisa

print("Wel-Come to Sanmina Lab for Automation Testing ")
rm = pyvisa.ResourceManager()
rm.list_resources()

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

print( "TIme : ",datetime.now())

import time

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")
