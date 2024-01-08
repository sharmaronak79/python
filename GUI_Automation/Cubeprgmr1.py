import pywinauto
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
def cubeprogrammer():
    print("Opening STM32 CubProgrammer........")

    app = Application(backend='uia').start(cmd_line=r"C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32CubeProgrammer.exe",timeout=20)
    time.sleep(13)

    app.connect(title='STM32CubeProgrammer')
    time.sleep(2)

    main_window = app.window(title_re = 'STM32CubeProgrammer')

    ConnectButton = main_window.child_window(title="Connect", auto_id="JavaFX184", control_type="Button").wrapper_object()
    ConnectButton.click()

    OpenfileButton = main_window.child_window(title="Open file", auto_id="JavaFX109", control_type="Button").wrapper_object()
    OpenfileButton.click_input()
    print('Open file clicked')

    ##Error form here
    Openfile_window = app.window(title_re = 'Open file')
    Openfile_window.print_control_identifiers()
    time.sleep(5)

    CloseButton = main_window.child_window(title="Close", control_type="Button").wrapper_object()
    CloseButton.click()

