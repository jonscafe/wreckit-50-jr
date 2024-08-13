import random
def random_hex(n, a):
    #a = random.randint(random.randint(10**(1-1), (10**1)-1), random.randint(10**(6-1), (10**6)-1))
    random.seed(a)
    range_start = 16**(n-1)
    range_end = (16**n)-1
    return random.randint(range_start, range_end)

from Crypto.Util.number import bytes_to_long, long_to_bytes
with open('output.txt', 'r') as f:
    ct = f.read()
ct = int(ct, 16)
ctl = long_to_bytes(ct).hex()
range_start = 10**(1-1)
range_end = (10**7)-1
for i in range(range_start, range_end):
    if i % 1000000 == 0:
        print(i)
    key = random_hex(len(ctl),i)
    pt = (long_to_bytes(ct ^ key))
    if b'WRECKIT50' in pt:
        print(pt)