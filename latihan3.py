#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : latihan3.py
@IDE         : PyCharm
@Date        : 29/11/2022 16:52
"""

spend = int(input('Masukan jumlah belanjaan anda: RM'))
current_year = int(input('Masukan tahun semasa: '))

if spend >= 35 and current_year == 2022:
    if spend < 50:
        print(f'Anda mendapat diskaun 5%')
        print(f'Jumlah yang perlu dibayar ialah RM{spend - (spend * 0.05)}')
    else:
        print(f'Anda mendapat diskaun 10%')
        print(f'Jumlah yang perlu dibayar ialah RM{spend - (spend * 0.1)}')

else:
    print(f'Anda tidak mendapat diskaun')
    print(f'Jumlah yang perlu dibayar ialah RM{spend}')