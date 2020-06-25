# python3
import math
class Heap:
    def __init__(self):
        self.heap = []
        self.swap = []

    def choice(self,i):
        if(self.heap[2*i+1]<self.heap[2*i+2]):
            return 2*i+1
        else:
            return 2*i+2


    def shiftdown(self,i):
        while(i<len(self.heap)):
            if((2*i+2)<len(self.heap) and self.heap[i]>self.heap[self.choice(i)]):
                value = (i,self.choice(i))
                shift = self.choice(i)
                self.heap[i],self.heap[self.choice(i)] = self.heap[self.choice(i)],self.heap[i]
            elif((2*i+1)<len(self.heap) and self.heap[i]>self.heap[2*i+1]):
                value  = (i,2*i+1)
                shift = 2*i+1
                self.heap[i],self.heap[2*i+1] = self.heap[2*i+1],self.heap[i]
            else:
                break
            self.swap.append(value)
            i = shift


    def insert(self,array):
        self.heap = array
        for index in range((len(self.heap)//2),-1,-1):
            self.shiftdown(index)
        return self.swap

def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    heap = Heap()
    return heap.insert(data)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
