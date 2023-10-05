import pywinauto
from pywinauto import application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.controls.win32_controls import ComboBoxWrapper

def open_TicsPro():
    print("Opening TicsPro....")
    Tics=application.Application().start("C:\Program Files (x86)\Texas Instruments\TICS Pro\TICS Pro.exe")
    time.sleep(7)
    dlg=Tics.window(title='TICSPro')
    dlg.print_control_identifiers()
