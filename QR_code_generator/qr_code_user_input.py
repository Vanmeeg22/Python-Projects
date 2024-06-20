import qrcode as qr

txt = input("Enter your QR message here: ")
# print(txt)
img = qr.make(txt)
img.save("txt.png")