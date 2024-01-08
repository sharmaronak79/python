import pywinauto
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
def cubeprogrammer():
    print("Opening STM32 CubProgrammer........")

    app = Application(backend='uia').start(cmd_line=r"C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32CubeProgrammer.exe",timeout=20)
    time.sleep(10)

    app.connect(title='STM32CubeProgrammer')
    time.sleep(1)

    main_window = app.window(title_re = 'STM32CubeProgrammer')

    #Click on Connect Button
    main_window.child_window(title="Connect", auto_id="JavaFX184", control_type="Button").click()

    #Click on Memory and File Editing
    main_window.child_window(auto_id="JavaFX23", control_type="Button").click()
    time.sleep(1)

    #Click on Erasing and Programming
    main_window.child_window(title="Erasing & programming", auto_id="JavaFX380", control_type="Button").click()
    time.sleep(3)


    # Close the Application
    # main_window.child_window(title="Close", control_type="Button").click()
