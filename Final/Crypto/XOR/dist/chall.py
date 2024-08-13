import random
FLAG = b'WRECKIT50{REDACTED}'

def random_hex(n):
    a = random.randint(random.randint(10**(1-1), (10**1)-1), random.randint(10**(7-1), (10**7)-1))
    random.seed(a)
    range_start = 16**(n-1)
    range_end = (16**n)-1
    return random.randint(range_start, range_end)

FLAG = FLAG.hex()
KEY = random_hex(len(FLAG))
c = str(hex(int(FLAG, 16)^KEY))[2:]
print("Ciphertext: %s"%c)
with open('output.txt', 'w') as f:
    f.write(c) 