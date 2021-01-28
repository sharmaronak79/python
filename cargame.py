
print("welcome to car the game ")
started = False
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already stared...")
        else: 
            started = True   
            print("car is started...")
    elif command == "stop":
        if not started:
            print("car is already stopped...")
        else:
            started = False
            print("car is stopped.")

    elif command == "help":
        print("""
        start - to start a car
        stop - to stop a car
        quit - to quit a game        
            """)
    elif command == "quit":
        break
    else:
        print("Sorry...I don't understand..")
