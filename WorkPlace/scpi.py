import socket
import time

import pyvisa

import variables as var

RCV_SZ = 2000


def canary_socket():
    print("Hello I am trying to connect to he Canary system...")
    TIMEOUT_VAL = 20000

    canary = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM)  # AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol
    canary.settimeout(TIMEOUT_VAL)

    IP4_ADDR = "192.168.0.30"  # canary system IP address
    PORT_NUM = 5555  # Socket PORT
    canary.connect((IP4_ADDR, PORT_NUM))  # API to connect with Canary main System

    canary.send("*IDN?\n".encode())
    time.sleep(0.1)  # Must add some delay to between send and receive else it will not give ant output
    RCV_DATA = canary.recv((RCV_SZ)).decode().rstrip()
    print(RCV_DATA)

    # canary.send(":rfall:status".encode())
    # time.sleep(5)
    # RCV_DATA = canary.recv((RCV_SZ)).decode().rstrip()
    # print(RCV_DATA)

    canary.send(":rf3:temp".encode())
    time.sleep(5)
    RCV_DATA = canary.recv((RCV_SZ)).decode().rstrip()
    print(RCV_DATA)


def canary_pyvisa():
    rm = pyvisa.ResourceManager()
    canary = rm.open_resource('TCPIP0::192.168.0.30::5555::SOCKET')
    canary.write_termination = '\n'
    canary.read_termination = '\n'
    time.sleep(1)

    # Below code is useful to check the system status  ON/OFF
    l1 = canary.read()
    l2 = canary.read()
    status = l1 + '\n' + l2
    print(status)
    if "on" in status:
        print("System is ON")
    else:
        print("System is FF")

    # Testing of all SCPI Commands

    # *IDN?
    data = canary.query('*IDN?')
    print(data)

    # :rfx:status
    canary.write(":rfall:status?")
    rfx_channel_status = canary.read()
    print(rfx_channel_status)
    var.AVAILABLE_MODULES = int(list(filter(str.isdigit, rfx_channel_status))[0])
    print('Available_modules : {0}'.format(var.AVAILABLE_MODULES))
    i = var.AVAILABLE_MODULES
    while i > 0:
        print(canary.read())
        i -= 1


    # :rfx:temp - This is a command to check temperature of particular RFModule where x is 1 to 12
    # here query return only the first line (till terminator) of buffer so used additional 3 read() to get all U3,U4 and U5 temperature
    # canary.write(":rf3:temp")
    # i = 4
    # while i > 0:
    #     print(canary.read())
    #     i -= 1

    # :rfall:temp, Here the value of i will be number of available RF modules * 4, if you want to see 6 modules temperature then i = 6*4 =24
    canary.write(":rfall:temperature?")
    i = (4 * var.AVAILABLE_MODULES)
    while i > 0:
        print(canary.read())
        i -= 1


    canary.write(":syste:temp?")
    print(canary.read())
    print(canary.read())
    print(canary.read())
    # print(canary.read())


    # lmk_tmp = canary.query(":system:lmktemperature?")
    # print(lmk_tmp)
    # lmk_tmp = list(lmk_tmp.split(" "))
    # print(lmk_tmp)
    # var.LMK_TEMP = lmk_tmp[4]
    # print(float(var.LMK_TEMP))

    rm.close()


def set_configuration():
    rm = pyvisa.ResourceManager()
    canary = rm.open_resource('TCPIP0::192.168.0.30::5555::SOCKET')
    canary.write_termination = '\n'
    canary.read_termination = '\n'
    time.sleep(0.1)

    canary.write(":system:configuration 2")
    time.sleep(2)
    canary.read()

    print('Configuration is set')
    rm.close()


def set_freq():
    rm = pyvisa.ResourceManager()
    canary = rm.open_resource('TCPIP0::192.168.0.30::5555::SOCKET')
    canary.write_termination = '\n'
    canary.read_termination = '\n'
    time.sleep(0.1)

    data = canary.query('*IDN?')
    print(data)

    canary.write(":rf3:freq 8000 20")
    time.sleep(3)
    canary.read()

    print('Frequency is set')
    rm.close()
