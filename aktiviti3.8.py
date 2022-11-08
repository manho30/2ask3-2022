#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author      : manho <manho30@outlook.my>
@Description :
@File        : aktiviti3.8.py
@IDE         : PyCharm
@Date        : 8/11/2022 17:11
"""

umur = int(input('Sila masukkan umur: '))

if umur > 30:
    print('Anda ialah seorang dewasa')

if umur > 14:
    print('Anda ialah seorang belia')

if umur > 12:
    print('Anda ialah seorang remaja')

if umur < 12:
    print('Anda ialah seorang kanak-kanak')