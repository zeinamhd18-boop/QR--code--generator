import qrcode
img = qrcode.make("http://www.google,com")
img.save("my-qr.png")
print("QR Code generated successfully!")
