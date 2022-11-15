#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : juakan_amal.py
@IDE         : PyCharm
@Date        : 15/11/2022 16:55
"""

print('****Pengiraan Komisen Bagi Program Jualan Amal')

buah = float(input('Masukkan jualan buah-buah RM: '))
minuman = float(input('Masukkan jualan minuman RM: '))
piakut = float(input('Masukkan jualan biskut RM:'))

jumlah = buah + minuman + piakut
print(f'\nJumlah jualan: RM {round(jumlah, 2)}')

if jumlah > 800:
    print('Komisen ialah 8%')
    komisem = 0.08

elif jumlah > 500:
    print('Komisen ialah 5%')
    komisem = 0.05

else:                               # Error found
    print('Komisen ialah 8%')
    komisem = 0.08

_jumlah = jumlah * komisem
_ = _jumlah / 6

print(f'Jumlah komisen RM: {round(_jumlah, 2)}')
print(f'Komisen untuk setiap ahli: RM {round(_, 2)}')
