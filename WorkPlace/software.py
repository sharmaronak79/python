
import pywinauto
import time
from pywinauto import application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.controls.win32_controls import ComboBoxWrapper


def open_Teraterm():
    print("Opening Tera Term....")

    # start an application
    TT = application.Application().start("C:/Program Files (x86)/teraterm/ttermpro.exe")
    time.sleep(1)  # going for sleep for 3 seconds

    # click on Serial
    TT.TeraTermNewconnection.Serial.click()

    # Very Useful to identify all controls , dropbox its number, name and all
    # TT.TeraTermReconnection.print_control_identifiers()

    TT.TeraTermNewconnection.Combobox4.click()  # From the above command we got to know that it is ComboBox4 and then we clicked it
    time.sleep(2)
    TT.TeraTermNewconnection.Combobox4.select(2)

    # click on OK button
    TT.TeraTermNewconnection.OK.click()

    # click on main menu's Setup and then clicked on Serial Port
    TT.COM3TeraTermVT.menu_item(u'&Setup->&Serialport').click()
    # on the Speed dropdown menu it writes baudrate as 115200
    TT.TeraTermSerialportsetupandconnection["Speed:Edit"].type_keys("115200")
    # after the baudrste is set clicked on NewSetting
    TT.TeraTermNewconnection.NewSetting.click()
    while 1:
        time.sleep(5)
        # TT.COM10TeraTermVT.connect()
        TT.COM10TeraTermVT.menu_item(u'&Edit->&Clearbiffer').click()


def open_TicsPro():
    print("Opening TicsPro....")
    tics = application.Application().start("C:\Program Files (x86)\Texas Instruments\TICS Pro\TICS Pro.exe")
    time.sleep(7)

    tics.TICSProLMX2485E.print_control_identifiers()

    tics.TICSProLMX2485E.HwndWrapper.click()

