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

    #
    # w_handle = pywinauto.findwindows.find_windows(title=u'STM32CubeProgrammer')
    # window = app.window(handle = w_handle)
    # window.wait('ready',timeout=10)
    #
    # window[u'Memory & File editingToolbar:Toolbar'].select()



    main_window = app.window(title_re = 'STM32CubeProgrammer')

    ConnectButton = main_window.child_window(title="Connect", auto_id="JavaFX184", control_type="Button").wrapper_object()
    ConnectButton.click()

    # memoryandfile = main_window.child_window(title="Memory & File editing", auto_id="JavaFX25", control_type="Text").wrapper_object()
    # memoryandfile.click_input()
    # time.sleep(3)

    ## To Select Memory and File Editing
    memoryandfile = main_window.child_window(auto_id="JavaFX23", control_type="Button").wrapper_object()
    memoryandfile.click_input()
    time.sleep(1)

    ## To select Erasing and Programming
    ersNprgrmng = main_window.child_window(title="Erasing & programming", auto_id="JavaFX380", control_type="Button").wrapper_object()
    ersNprgrmng.click_input()
    time.sleep(1)

    ## Way1
    # browse = main_window.child_window(title="Browse", auto_id="JavaFX657", control_type="Button").wrapper_object()
    # browse.click_input()
    # hndl = pywinauto.findwindows.find_windows(title= u'Open File to program')
    # window = app.window(handle = hndl)
    #
    # window.Treeview.get_item(u'Desktop').click()

    ## Way2
    file_path_text = main_window.child_window(title="File path", auto_id="JavaFX642", control_type="Text")
    file_path_text.set_edit_text(r'C:\Users\ronakkumar_sharma\Desktop\CanaryDesign')

    # main_window.child_window(auto_id="JavaFX647", control_type="Edit").type_keys(r'Ronak')
    # main_window.FilepathEdit["Filepath:Edit"].type_keys(r'C:\Users\ronakkumar_sharma\Desktop\GUI_Automation\My_Test.hex')
    # main_window.child_window(title="File path", auto_id="JavaFX642", control_type="Text").type_keys(r'C:\Users\ronakkumar_sharma\Desktop\Canary_Design\Beta_RF_Firmware/canary_app_1_0_0.hex')

    ## To Select path to the hex file
    # filepath = main_window.child_window(title="File path", auto_id="JavaFX642", control_type="Text").send_keys(r'C:\Users\ronakkumar_sharma\Desktop\GUI_Automation\My_Test.hex')
    # main_window.FilepathEdit["Filepath:Edit"].type_keys(r'C:\Users\ronakkumar_sharma\Desktop\GUI_Automation\My_Test.hex')
    # browse = main_window.child_window(title="Browse", auto_id="JavaFX657", control_type="Button").wrapper_object()
    # browse.click_input()

    # filepath = main_window.child_window(auto_id="JavaFX647", control_type="Edit").type_keys(r'C:\Users\ronakkumar_sharma\Desktop\GUI_Automation\My_Test.hex')
    # main_window["Filepath:Edit"].type_keys(r' ')
    # openfilwindow_handle = pywinauto.findwindows.find_windows(title=u'Open File to program')
    # openfilwindow = app.window(handle=openfilwindow_handle)
    # opflwnd = app.window(title = 'Open File to program')
    # opflwnd.print_control_identifiers()
    # openfilwindow.Desktop.select()

    # main_window.print_control_identifiers()

    # OpenfileButton = main_window.child_window(title="Open file", auto_id="JavaFX109", control_type="Button").wrapper_object()
    # OpenfileButton.click_input()
    # print('Open file clicked')
    #
    #
    # Openfile_window = app.window(title_re = 'Open file')
    # Openfile_window.print_control_identifiers()
    # time.sleep(5)

    # CloseButton = main_window.child_window(title="Close", control_type="Button").wrapper_object()
    # CloseButton.click()

