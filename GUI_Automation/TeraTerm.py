from datetime import time

import pywinauto
import time
from pywinauto import application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.controls.win32_controls import ComboBoxWrapper

def teraterm():
    print("Opening Tera Term....")

    #start an application
    TT= Application(backend='win32').start("C:/Program Files (x86)/teraterm/ttermpro.exe")
    time.sleep(5) #going for sleep for 3 seconds

    #clcik on Serial
    TT.TeraTermNewconnection.Serial.click()

    #select USB Port
    TT.TeraTermNewconnection.Combobox4.click() # From the above command we got to know that it is ComboBox4 and then we clicked it
    TT.TeraTermNewconnection.Combobox4.select(1) # Here 1 is the index of USB port , It might be different if more USB port is connected so check manually by opening the app and change accordingly
    time.sleep(2)

    #click on OK button
    TT.TeraTermNewconnection.OK.click()
    time.sleep(2)

    #click on main menu's Setup and then clicked on Serial Port
    TT.COM3TeraTermVT.menu_item(u'&Setup->&Serialport').click()
    #on the Speed dropdown menu it writes baudrate as 115200
    TT.TeraTermSerialportsetupandconnection["Speed:Edit"].type_keys("115200")

    #after the baudrste is set clicked on NewSetting
    TT.TeraTermNewconnection.NewSetting.click()
    print("Reset the Nucleo Board")# Here have to write a script topower cycle the RF  module
    time.sleep(5) #Here we have to reboot the nucleo board
    print("Firmware is sending....")


    #Sending a Firmware by selectig a hex file path
    TT.COM3TeraTermVT.menu_item(u'&File->&Sendfile').click()
    send_file_win = TT.window(title = 'Tera Term: Send file')
    # send_file_win.print_control_identifiers()
    send_file_win.ComboBox.select("Desktop")
    send_file_win.ComboBox.select("Canary_Design")
    send_file_win.ComboBox.select("Beta_RF_Firmware")
    send_file_win.child_window(class_name="Edit").type_keys("canary_app_1_0_0.hex")
    send_file_win.child_window(title="&Open", class_name="Button").click()

    #To clear the screen
    #TT.COM10TeraTermVT.menu_item(u'&Edit->&Clearbuffer').click()

    # TT.kill()
