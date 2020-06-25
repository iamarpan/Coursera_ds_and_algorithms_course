# Uses python3
def calc_fib(n):
    if(n<=1):
        return n
    else:
        a = 0 
        b = 1
        for _ in range(n-1):
            c = a+b
            a = b
            b = c
        return c 
    
n = int(input())
print(calc_fib(n))
