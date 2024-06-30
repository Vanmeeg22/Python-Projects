import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 5,)

msg = input("Enter your QR message here: ")
qr.add_data(msg)
qr.make(fit=True)
img = qr.make_image(fill_color = "#00B7EB", back_color = "black")
img.save("qr.png")