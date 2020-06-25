# Uses python3
import sys

def fibonacci_sum_naive(n):
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
    if(n>59):
        s = sum(arr)
        remainder = n%len(arr)
    return (s + sum(arr[0:remainder+1]))%10
if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))
