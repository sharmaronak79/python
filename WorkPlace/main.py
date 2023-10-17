# #This is for test equipment for the Lab

# import pyvisa
# import datetime
# import time
import variables as var
# # print("Wel-Come to Sanmina Lab for Automation Testing ")
# # rm = pyvisa.ResourceManager()
# # print(rm.list_resources())
# # PS_HMP4040=rm.open_resource('ASRL18::INSTR')
# # print(PS_HMP4040.query("*IDN?"))
# # time.sleep(1)
# # print("\n3 Seconds Elapsed...")
# # print(PS_HMP4040.query("*IDN?"))
# # PS_HMP4040.write('*RST')
# # PS_HMP4040.write('*CLS')
# # PS_HMP4040.write('INST OUT1')
# # PS_HMP4040.write('VOLT 12')
# # PS_HMP4040.write('CURR 0.1')
# # PS_HMP4040.write('OUTP 1')
# #
# # #For Channel 2
# # PS_HMP4040.write('INST OUT2')
# # PS_HMP4040.write('VOLT 10')
# # PS_HMP4040.write('CURR 0.2')
# # PS_HMP4040.write('OUTP 1')
# #
# # for v in range(5,10,1):
# #     PS_HMP4040.write('VOLT ,'+ str(v) +',0.2')
# #     time.sleep(2)
# #     print(v)
#
#
import ronak as rk
# #rk.name("Jwal")
# #rk.process_value()
# #rk.open_Teraterm()
# #rk.open_TicsPro()


import scpi as sc
import software as sft
sc.canary_pyvisa()
# print(f"Total available modules are : {sc.AVAILABLE_MODULES}")

print("LMK Temperature is : {} C"  .format(var.LMK_TEMP))
print("Available modules are : {}" .format(var.AVAILABLE_MODULES))
