import qrcode

text = 'syh'
qr = qrcode.make(text)
qr.save('syh.jpg')