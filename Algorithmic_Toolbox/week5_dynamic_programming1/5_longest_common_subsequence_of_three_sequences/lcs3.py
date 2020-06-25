#Uses python3

import sys
def lcs2(a,b,c):
    cache = [[[-1 for _ in range(len(c)+1)] for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            for k in range(len(c)+1):
                if(i==0):
                    cache[i][j][k]=0
                elif(j==0):
                    cache[i][j][k]=0
                elif(k==0):
                    cache[i][j][k]=0
                else:
                    if(a[i-1]==b[j-1]==c[k-1] ):
                        cache[i][j][k] = 1 + cache[i-1][j-1][k-1]
                    else:
                        cache[i][j][k] = max(cache[i-1][j][k],cache[i][j-1][k],cache[i][j][k-1])
    return cache[len(a)][len(b)][len(c)]

def lcs3(a, b, c):
    return lcs2(a,b,c)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a,b,c))
