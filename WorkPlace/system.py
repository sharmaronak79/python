import socket
RCV_SZ = 2000
def canary():
    print("Hello I am trying to connect to he Canary system...")
    TIMEOUT_VAL = 20000

    canary= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    canary.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)

    canary.settimeout(TIMEOUT_VAL)

    IP4_ADDR= "192.168.0.30"
    PORT_NUM = 5555
    canary.connect((IP4_ADDR,PORT_NUM))

    canary.send("*IDN?\n".encode())

    RCV_DATA = canary.recv((RCV_SZ)).decode().rstrip()
    print(RCV_DATA)
