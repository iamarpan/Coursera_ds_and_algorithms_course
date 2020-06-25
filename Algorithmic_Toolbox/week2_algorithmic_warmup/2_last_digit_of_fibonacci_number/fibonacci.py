def last_fibonacci_digit(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        f1 = 0
        f2 = 1
        for a in range(2,n+1):
            current = (f1 + f2)%10
            f1 = f2
            f2 = current
    return current

if __name__ == '__main__':
    n = int(input())
    print(last_fibonacci_digit(n))

