#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    cache = [[0 for b in range(len(b)+1)]for a in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if(i==0):
                cache[i][j]=0
            elif(j==0):
                cache[i][j]=0
            else:
                if(a[i-1]==b[j-1]):
                    cache[i][j]=1+cache[i-1][j-1]
                else:
                    cache[i][j] = max(cache[i-1][j],cache[i][j-1])

    return cache[len(a)][len(b)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
