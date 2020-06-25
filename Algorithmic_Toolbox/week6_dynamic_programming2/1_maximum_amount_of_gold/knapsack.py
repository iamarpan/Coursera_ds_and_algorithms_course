# Uses python3
import sys

def optimal_weight(W, w):
    cache = [[0 for _ in range(W+1)] for a in range(len(w))]
    for i in range(len(w)):
        for j in range(W+1):
            if(j==0):
                cache[i][j]=0
            elif(i==0):
                if(j-w[i]>=0):
                    cache[i][j]=w[i]
                else:
                    cache[i][j]=0
            else:
                if(j-w[i]>=0):
                    cache[i][j]=max(cache[i-1][j],w[i]+cache[i-1][j-w[i]])
                else:
                    cache[i][j]=cache[i-1][j]
    return cache[len(w)-1][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W,w))
