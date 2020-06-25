# Uses python3
import sys

def get_change(m):
    coins = [10,5,1]
    count = 0
    for coin in coins:
        if(m//coin>=1):
            count+=m//coin
            m = m%(coin*(m//coin))

    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
