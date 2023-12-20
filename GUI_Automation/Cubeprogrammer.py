import pywinauto
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
def cubeprogrammer():
    print("Opening STM32 CubProgrammer........")

    # Application(backend='uia').start(cmd_line=r"C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeProgrammer\bin\STM32CubeProgrammer.exe").connect(title="STM32CubeProgrammer")
    app = Application(backend='uia').connect(title='STM32CubeProgrammer')
    
