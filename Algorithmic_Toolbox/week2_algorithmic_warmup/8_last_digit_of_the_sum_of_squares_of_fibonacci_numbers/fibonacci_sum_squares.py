# Uses python3
import sys
import math
def fibonacci_square_sum_naive(n):
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
    arr = list(map(lambda x:x**2,arr))

    divider = int(n/(len(arr)))
    remainder = n%(len(arr))
    return (sum(arr[:remainder+1]) + divider*sum(arr))%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_square_sum_naive(n))
