#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : aktiviti3.4.py
@IDE         : PyCharm
@Date        : 8/11/2022 17:20
"""

terus = True

while terus:

print('Jawab soalan berikut.\n')

# soalan 1
print('Soalan 1')
soalan1 = input('6 ialah faktor bagi 96. Jawab YA atau TIDAK.')

if soalan1 == 'YA':
    print('True\n\n')
else:
    print('False\n\n')

# soalan 2
print('Soalan 2\n')
soalan2 = float(input('1 - 3 x 5/24'))

if soalan2 == 0.375:
    print('True\n\n')
else:
    print('False\n\n')

# soalan 3
print('Soalan 3\n')
soalan3 = (input('''Adakah ungkapan berikut "Betul" atau "Salah".
6+(-7) < 3-(-4)'''))

if soalan3 == 'Betul':
    print('True\n\n')
else:
    print('False\n\n')