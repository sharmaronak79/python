#module is nothin but the creating some code and put in one other file and then 
# call a function from that created file to current file
# here i have creatred some function of converters in conveter.py and imort them to my module file 
# so it like header file we create in c language and include it in our surc code
#here the key words are used are import
import converter
converter.kg_to_lbs()
from converter import lbs_to_kg
lbs_to_kg()
s=[10,55,30,70,44]
from find_max import find_max
find_max(s)
import file
file.school()
file.college()