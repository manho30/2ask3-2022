#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : aktiviti3.10.py
@IDE         : PyCharm
@Date        : 8/11/2022 17:15
"""

num = int(input('Masukan nombor jadual sifar darab anda: '))

for i in range(12):
    print(f'{i+1} x {num} = {(i+1) * num}')