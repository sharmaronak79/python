import pywinauto
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

print('I am cubeprograer...')

def open():
    print('Opening Cube Programmer....')
    # app = Application(backend='uia').connect(title='STM32CubeProgrammer')
    app = Application(backend='uia').start(cmd_line=r"C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32CubeProgrammer.exe",timeout=20)
    time.sleep(10)
    app.connect(title='STM32CubeProgrammer')
    time.sleep(2)
    main_window = app.window(title_re="STM32CubeProgrammer")
    # main_window.print_control_identifiers()
    connect = main_window.child_window(title="Connect", auto_id="JavaFX184", control_type="Button").wrapper_object()
    connect.click()
    time.sleep(2)
    openfile = main_window.child_window(title="Open file", auto_id="JavaFX108", control_type="Text").wrapper_object()
    # openfile.click_input() // Gives an error
    time.sleep(2)
    openfile_window = openfile.window(title_re = 'Openfile')
    openfile_window.print_control_identifiers()
  
