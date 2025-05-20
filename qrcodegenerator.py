import qrcode


data = input('Enter Url/Link: ').strip()
file = input ('enter file name: ').strip()

qr = qrcode.QRCode(box_size = 10 , border = 5)
qr.add_data(data)

image = qr.make_image(fill_color = "black" , back = "white")
image.save(file + '.jpg')

print(f' Your QR code has been saved as {file}.jpg')