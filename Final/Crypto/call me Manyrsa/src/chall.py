from Crypto.Util.number import *

str = ["????"]

p,q = getPrime(512), getPrime(512)
e = 65537

for str in str:
    flag = 'WRECKIT50{'+str+'}'
    m = bytes_to_long(flag.encode())
    n = p*q
    c = pow(m,e,n)

    print(f'n = {n}')
    print(f'c = {c}')
    print(f'pplusq = {p+q}\n')