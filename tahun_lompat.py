#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : tahun_lompat.py
@IDE         : PyCharm
@Date        : 8/11/2022 16:54
"""

tahun = int(input('Masukan tahun untuk semak: '))

if tahun % 4 == 0:
    if tahun % 100 == 0:
        if tahun % 400 == 0:
            print(f'{tahun} ialah tahun lompat.')
        else:
            print(f'{tahun} bukan tahun lompat.')
    else:
        print(f'{tahun} ialah tahun lompat.')
else:
    print(f'{tahun} bukan tahun lompat.')

