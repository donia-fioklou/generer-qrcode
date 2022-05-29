# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:43:28 2021

@author: ACER
"""

import qrcode

qr = qrcode.QRCode(version=3,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=3,
                   border=5)
qr.add_data("donia fioklou")
qr.make(fit=True)

img =qr.make_image(fill_color="red",back_color="black")

img.save("qrcode.png")





