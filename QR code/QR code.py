#Author: Devashy Patel
#Date: 12/6/2025
import qrcode,PIL

text = input("Enter the text to be converted to QR code: ")
img = qrcode.make(text)
img.save("QR code.PNG")
