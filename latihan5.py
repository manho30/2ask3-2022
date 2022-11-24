#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : latihan5.py
@IDE         : PyCharm
@Date        : 24/11/2022 21:25
"""

i = 0
total = 0

mark = int(input('Masukan markah anda.'))

while mark != 0:
    i = i + 1

    if i == 1:
        lowest = mark
        highest = mark

    if mark < lowest:
        lowest = mark

    if mark > highest:
        highest = mark

    total = total + mark
    balance = (total / i).__round__(2)
    mark = int(input('Masukan markah anda.'))
else:
    print(f"""Markah tertinggi ialah {highest}
Markah terendah ialah {lowest}
Markah purata ialah {balance}""")
