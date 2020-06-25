# Uses python3
import sys

def gcd_naive(a, b):
    if(a==0):
        return b

    return gcd_naive(b%a,a)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
