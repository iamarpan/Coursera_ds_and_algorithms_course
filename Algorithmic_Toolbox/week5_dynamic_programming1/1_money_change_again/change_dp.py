# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1,3,4]
    cache = [m+1 for a in range(m+1)]
    cache[0] = 0
    for index in range(1,m+1):
        for coin in coins:
            if(index-coin>=0):
                cache[index] = min(cache[index-coin]+1,cache[index])
    return cache[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
