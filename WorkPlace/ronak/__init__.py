import time
from time import sleep
import os

# Datalogging: create a time-stamped file
dateString = time.strftime("%Y-%m-%d_%H%M")
filepath = "./" + dateString + ".csv"


def name(string):
    print(string)
    print("work done")

def process_value():
    val = float(input(("Enter value : ")))
    i=1
    print("Value(v)    Squr(v)     Cube(V)\n")
    while (i<=val) :

        print("{}           {}          {}".format(i,i*i,i*i*i))
        #print(f'{i}  {i*i}  {i*i*i}')

        # Write results to a file
        with open(filepath, "a") as file:
            if os.stat(filepath).st_size == 0:  # if empty file, write a nice header
                file.write("Value(v)    Sqr(v)     Cube(V)\n")
            file.write("{}              {}              {}\n".format(i,i*i,i*i*i))  # log the data
        file.close()

        i+=1
        sleep(0.5)



    print("work done")
