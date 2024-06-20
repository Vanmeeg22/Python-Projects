import qrcode as qr

img = qr.make("My name is Vanmeeg")
img.save("msg.png")