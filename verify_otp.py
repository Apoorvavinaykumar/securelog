# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 00:54:07 2024

@author: User
"""

def verify_OTP(actual,entered):
    if(actual==entered):
        print("verfication succeeded")
    else:
        print("incorrect OTP,try again")
        
verify_OTP(1234, 1234)