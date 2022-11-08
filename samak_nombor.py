#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : samak_nombor.py
@IDE         : PyCharm
@Date        : 8/11/2022 16:59
"""

num = int(input('Masukan satu nombor: '))

if num == 0:
    print('O is not accepted!')
    exit()

else:
    if num > 0:
        print(f'Nombor {num} ialah nombor possitive.')

        if num % 2 == 0:
            print(f'Nombor {num} ialah nombor genap.')
        else:
            print(f'Nombor {num} ialah nombor gamjil.')
    else:
        print(f'Nombor {num} ialah nombor negative.')
