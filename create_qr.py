import qrcode

text = "Hill Pyro"
qr = qrcode.make(text)
qr.save('hill.jpg')