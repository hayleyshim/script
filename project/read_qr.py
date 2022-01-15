from pyzbar.pyzbar import decode
from PIL import Image
pic = Image.open("syh.png")
qr = decode(pic)
text = qr[0].data.decode()
print("Text for your qr is: {}".format(text))
