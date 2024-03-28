import time
import threading

def square(A):
    for num in A:
        print(f'Square of {num} is  : {num * num}')
        time.sleep(0.2)
def cube(A):
    for num in A:
        print(f'Cube of {num} is : {num*num*num}')
        time.sleep(0.2)



T = time.time()

print(f'start time: {T}')

A=[1,2,3,4,5,6,7,8,9]

# square(A)
# cube(A)

t1 = threading.Thread(target=square,args=(A,))
t2 = threading.Thread(target=cube,args=(A,))

t1.start()
t2.start()

t1.join()
t2.join()



print("Execution is Finished . . .")
print(f'Total time taken for execution is : {time.time() - T}')
