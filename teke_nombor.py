#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : teke_nombor.py
@IDE         : PyCharm
@Date        : 15/11/2022 17:13
"""

from time import sleep

print('*** PERMAINAN MENEKA NOMBOR***')

rahsia = 90
_ = True

while _:
    nombor = int(input('Masukkan nombor tekaan anda:'))
    if rahsia == nombor:
        for i in range(5):
            _ = False
            print('Syabas!')
            sleep(1)
    elif rahsia < nombor:
        print('Nombor tekaan lebih besar daripada nombor rahsia')
    else:
        print('Nombor tekaan lebih kecil daripada nombor rahsia')
else:
    print('Terima kasih! Anda telah teka nombor yang betul.')
