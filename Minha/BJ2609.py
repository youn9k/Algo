'''
from math import gcd, lcm
'''
n, m = map(int, input().split())

def gcd(n, m):
    while 1:
        q=n/m
        r=n%m
        if r==0:
            break
        n=m
        m=r
    return int(m)

def lcm(n, m):
    gd = gcd(n, m)
    return int((n/gd)*(m/gd)*gd)

        
print(gcd(n, m))
print(lcm(n, m))