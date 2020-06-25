# Uses python3
import sys
import time
def optimal_sequence(n):
    cache = [-1 for a in range(n+1)]
    cache[0]=0
    cache[1]=0
    element=[]
    m=n
    chosen={}
    for index in range(2,n+1):
        min_2 = n+1
        min_3 = n+1
        if(index%2==0):
            min_2 = cache[index//2]
        if(index%3==0):
            min_3 = cache[index//3]
        minimum = min(min_2,min_3,cache[index-1])
        cache[index] = 1+minimum 
    print(cache[-1])
  #  return reversed(sequence)


if __name__ == '__main__':
    optimal_sequence(1000000)
#input = sys.stdin.read()
#n = int(input)
#n=96234
#sequence = list(optimal_sequence(n))
#print(len(sequence) - 1)
#for x in sequence:
 #   print(x, end=' ')
