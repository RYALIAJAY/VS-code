import random
import string
def generate(size):
    otp=''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits)for n in range(size)])
    return otp

password=generate(8)
print(password)