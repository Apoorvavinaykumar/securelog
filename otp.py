import random
def generate_otp(l):
    print("generate otp")
    otp=''.join(random.choices('0123456789',k=l))
    return otp 
otp=generate_otp(4)
print("The Generated OTP is :",otp )