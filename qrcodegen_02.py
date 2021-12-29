import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)
qr.add_data('https://www.google.com')
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="black")

img.save("qrcode_02.png")