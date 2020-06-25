def fibn(n,m):
    a = 0
    b = 1
    arr = [0,1]
    if(n<2):
        return n
    for _ in range(2,n+1):
        c = a + b
        a = b
        b = c
        arr.append(c%m)
        if(len(arr)%2==0 and (arr[0:int(len(arr)/2)]==arr[int(len(arr)/2):])):
            return arr[n%int(len(arr)/2)]

    return c%m
if __name__ == '__main__':
    n,m = map(int, input().split())
    print(fibn(n,m))

