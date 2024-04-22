# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 15:29:31 2024

@author: Anusha V
"""

import random
def generate_captcha(l):
    print("genrate captcha")
    captcha=''.join(random.choices('abcdefghijklmnopqrstuvwxyz',k=l))
    return captcha
captcha=generate_captcha(5)
print(captcha)