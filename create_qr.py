import qrcode

text = 'SYH'
qr = qrcode.make(text)
qr.save('syh.jpg')