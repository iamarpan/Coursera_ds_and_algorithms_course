# Uses python3
import sys
def gcd(a,b):
    if(a==0):
        return b
    return gcd(b%a,a)

def lcm_naive(a, b):
    if(a==0 or b==0):
        return 0
    lcm = int((a*b)/gcd(a,b))
    return lcm

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

