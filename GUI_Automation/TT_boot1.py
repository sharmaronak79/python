from datetime import time

import pywinauto
import time
from pywinauto import application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

def boot_image():
    TT =Application().connect(title="COM8 - Tera Term VT")
    terminal = TT.window(title="COM8 - Tera Term VT")
    TT.COM8TeraTermVT.menu_item(u'&Edit->&Clearbuffer').click()
    terminal.click()
    terminal.type_keys("{ENTER}")
    time.sleep(3)
    if "App>" in terminal:
        terminal.type_keys("reset")
        time.sleep(2)
        terminal.type_keys("{ENTER}")
    terminal.type_keys(u"boot F",with_spaces=True)
    time.sleep(3)
    terminal.type_keys("{ENTER}")
    time.sleep(5)
    print("Factory image is booted")
