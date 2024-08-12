from Crypto.Util.number import *
from secret import flag

getAttr = getPrime(128)

def primedet(bit):
    las_pas = 2**2048 + getPrime(bit) + getAttr
    las_pas |= 1
    while True:
        if(isPrime(las_pas)): return las_pas
        las_pas+=2

def genpq():
    p = primedet(512)
    q = primedet(512)
    return p, q

if __name__ == '__main__':
    p,q = genpq()
    e = 0x10001
    c = pow(bytes_to_long(flag), e, p*q)
    with open("output.txt","w") as f:
        f.write(f'{p*q=}\n')
        f.write(f'{e=}\n')
        f.write(f'{c=}\n')