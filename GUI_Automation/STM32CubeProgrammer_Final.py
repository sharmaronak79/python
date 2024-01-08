import pywinauto
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

def cubeprogrammer():
    print("Opening STM32 CubProgrammer........")

    app = Application(backend='uia').start(cmd_line=r"C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32CubeProgrammer.exe",timeout=20)
    time.sleep(10)

    app.connect(title='STM32CubeProgrammer')

    main_window = app.window(title_re = 'STM32CubeProgrammer')

    #Click on Connect Button
    main_window.child_window(title="Connect", auto_id="JavaFX184", control_type="Button").click()

    #Click on Memory and File Editing
    main_window.child_window(auto_id="JavaFX23", control_type="Button").click()

    #Click on Erasing and Programming
    main_window.child_window(title="Erasing & programming", auto_id="JavaFX380", control_type="Button").click()

    # Writing a filepath and start programming
    main_window.child_window(auto_id="JavaFX644", control_type="ComboBox").click_input() #this will click on Edit box
    send_keys("^a")  # Press CTRL + a
    send_keys("{VK_DELETE}") # Press Delete button
    main_window[u'ComboBox:Edit'].type_keys(r"C:\Users\ronakkumar_sharma\Desktop\Boot_and_App\Bootloader.hex") # Write a file path
    main_window.StartProgramming.click() # Click on Start Programming
    time.sleep(4) # wait to complete the download
    send_keys("{ENTER}") # once it is done , Hit the Enter

    # Close the Application
    main_window.child_window(title="Close", control_type="Button").click()
    
