import pywinauto
from pywinauto import application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.controls.win32_controls import ComboBoxWrapper

def open_Teraterm():
    print("Opening Tera Term....")
    # out = os.getcwd()
    # print("Current working directory is:", out)
    # TT = os.chdir("C:/Program Files (x86)/teraterm")
    # out = os.getcwd()
    # print("Current working directory is:", out)

    #start an application
    TT= application.Application().start("C:/Program Files (x86)/teraterm/ttermpro.exe")
    time.sleep(2) #going for sleep for 3 seconds
    #clcik on Serial
    TT.TeraTermNewconnection.Serial.click()

    dropdown=TT.TeraTermNewconnection.Serial(control_name="Port:")
    dropdown.click_input()
    dropdown.select(2)
    #TT.TeraTermNewconnection.Port.select("USB Serial")
    #TT.Teratermnewconnection["port:Edit"].ComboBoxWrapper.select("USBserial")
    #click on OK button
    TT.TeraTermNewconnection.OK.click()
    #click on main menu's Setup and then clicked on Serial Port
    TT.COM3TeraTermVT.MenuItem(u'&Setup->&Serialport').click()
    #on the Speed dropdown menu it writes baudrate as 115200
    TT.TeraTermSerialportsetupandconnection["Speed:Edit"].type_keys("115200")
    #after the baudrste is set clicked on NewSetting
    TT.TeraTermNewconnection.NewSetting.click()
