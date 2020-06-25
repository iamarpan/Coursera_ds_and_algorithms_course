# python3
import sys
import pdb

def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.insert(0,0)
    stops.append(distance)
    i=0
    value = tank
    refill = 0
    while(i<len(stops)-1):
        if(tank<(stops[i+1]-stops[i])):
            return -1
        elif(tank>=(stops[i+1]-stops[i])):
            tank = tank- (stops[i+1]-stops[i])
            i+=1
            if((i!=len(stops)-1) and tank<(stops[i+1]-stops[i])):
                refill+=1
                tank = value

    return refill

if __name__ == '__main__':
    d = int(input())
    m = int(input())
    n = int(input())
    stops =list(map(int,input().split()))
    print(compute_min_refills(d, m, stops))
