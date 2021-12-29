import qrcode

my_qrcode = qrcode.make("https://www.google.com")

my_qrcode.save("qrcode.png")