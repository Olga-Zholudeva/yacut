import string
import random

N = 6
res = ''.join(random.choices(string.ascii_lowercase, k=6))
print(res)