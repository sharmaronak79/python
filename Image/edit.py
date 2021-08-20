from PIL import Image

jwal=Image.open('j.jpg')

jwal

jwal.size

jwal.filename

jwal.format_description

jwal.crop((0,0,100,100))

spn = Image.open("s.jpg")

spn

spn.size

x=220
y=70
w=959
h=1280

spn2=spn.crop((x,y,w,h))

spn2

spn2.size

jwal.size

spn2.resize((640,640))

spn2.putalpha(128)

spn2

jwal.paste(spn2,(0,0),spn2)

rr=Image.open("rr.jpg")

rrnew

rrnew.putalpha(90)

rrnew



spn2.size

jwal.size

rrnew.size

rsz=rrnew.resize((640,640))

spnrsz=spn2.resize((640,640))

jwal.paste(spnrsz,(0,0),spnrsz)

jwal

