# Uses python3
import sys
import math
def fibonacci_partial_sum_naive(m,n):
    arr = [0,1]
    a = 0
    b = 1
    s = 0
    remainder = n
    for _ in range(2,60):
        c = a + b
        a = b
        b = c
        arr.append(c%10)
    s = sum(arr[m%len(arr):]) + sum(arr[:(n+1)%len(arr)]) + sum(arr)*int((n-m)/len(arr)) - sum(arr)
    return s%10

if __name__ == '__main__':
    m,n = map(int,input().split())
    print(fibonacci_partial_sum_naive(m,n))
