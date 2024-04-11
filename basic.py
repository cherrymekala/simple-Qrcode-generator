import segno

qrcode=segno.make_qr("Hello bob..!")
qrcode.save("transparent_bob.png",scale=5,dark="#00008bcc",light="#ccccffcc",quiet_zone="#d3d3d377")