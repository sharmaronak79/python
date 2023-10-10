import socket
RCV_SZ = 2000
def canary():
    print("Hello I am trying to connect to he Canary system...")
    TIMEOUT_VAL = 20000

    canary= socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol
    canary.settimeout(TIMEOUT_VAL)

    IP4_ADDR= "192.168.0.30" #caary system IP address
    PORT_NUM = 5555 #Socket PORT
    canary.connect((IP4_ADDR,PORT_NUM)) #API to connect with Canary main System

    canary.send("*IDN?\n".encode())
    time.sleep(0.1) #Must add some delay between send and receive else it will not give an output
    RCV_DATA = canary.recv((RCV_SZ)).decode().rstrip()
    print(RCV_DATA)


###############################################################################################
def canary2():
    rm = pyvisa.ResourceManager()
    canary = rm.open_resource('TCPIP0::192.168.0.30::5555::SOCKET')
    time.sleep(3)
    canary.write("*IDN?")
