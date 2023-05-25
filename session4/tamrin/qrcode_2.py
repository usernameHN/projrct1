import qrcode

neme = input("enter your name :")
phone_number = input("enter your phone number :")

content = f"name : {neme} , phone{phone_number}"

qr = qrcode.QRCode(version=1 ,box_size=10 , border=5)
qr.add_data(content)
qr.make(fit=True)

img = qr.make_image(fill_color = "black" , back_color = "white")
img.save("qrcode.png")



