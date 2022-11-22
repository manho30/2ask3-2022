#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : latihan1.py
@IDE         : PyCharm
@Date        : 22/11/2022 17:31
"""


mark = int(input('Masukan markah anda: '))

if mark >= 85:
    print(f'Anda mencaoai Tahap Pencapaian 3 dan Kelas Lanjutan')
elif mark >= 65:
    print(f'Anda mencaoai Tahap Pencapaian 2 dan Kelas Pertengahan')
else:
    print(f'Anda mencaoai Tahap Pencapaian 1 dan Kelas Permulaan')