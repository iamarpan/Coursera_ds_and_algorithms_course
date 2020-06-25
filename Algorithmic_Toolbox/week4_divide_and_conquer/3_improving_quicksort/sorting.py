# Uses python3
import sys
import random

def partition3(array, l, r):
    #write your code here
    lt = l
    gt = r
    pivot = array[l]
    i=l
    while(i<=gt):
        if(array[i]<pivot):
            array[i],array[lt] = array[lt],array[i]
            lt+=1
            i+=1
        elif(array[i]>pivot):
            array[i],array[gt] = array[gt],array[i]
            gt-=1
        else:
            i+=1
    return lt,gt


def randomized_quick_sort(array, l, r):
    if(l<r):
        k = random.randint(l,r)
        array[k],array[l] = array[l],array[k] 
        lt,gt = partition3(array, l, r)
        randomized_quick_sort(array, l, lt-1);
        randomized_quick_sort(array, gt+1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *array= list(map(int, input.split()))
    randomized_quick_sort(array, 0, n - 1)
    for x in array:
        print(x, end=' ')
