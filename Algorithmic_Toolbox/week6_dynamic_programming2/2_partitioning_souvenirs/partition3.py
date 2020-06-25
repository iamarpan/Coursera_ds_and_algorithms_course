# Uses python3
import sys
import itertools
def isKPartitionPossibleRec(arr, subsetSum, taken, subset, K, N, curIdx, limitIdx):
    if subsetSum[curIdx] == subset:
        if(curIdx == K-2):
            return 1
        return isKPartitionPossibleRec(arr,subsetSum,taken,subset,K,N,curIdx+1,N-1)
    for i in range(limitIdx,-1,-1):
        if(taken[i]):
            continue
        tmp = subsetSum[curIdx] + arr[i]

        if(tmp<=subset):
            taken[i]= 1
            subsetSum[curIdx]+=arr[i]
            nxt = isKPartitionPossibleRec(arr,subsetSum,taken,subset,K,N,curIdx,i-1)
            taken[i]=0
            subsetSum[curIdx]-=arr[i]
            if(nxt):
                return 1
    return 0

    

def partition3(arr):
    k=3
    N = len(arr)
    if(k==1):
        return True
    if(N<k):
        return False
    add = 0
    for i in range(N):
        add+=arr[i]
    if(add%k!=0):
        return 0

    subset = add//k
    subsetSum = [0]*k
    taken = [0]*N

    for i in range(k):
        subsetSum[i]=0

    for i in range(N):
        taken[i] = False
    subsetSum[0] = arr[N-1]
    taken[N-1] = True

    return isKPartitionPossibleRec(arr,subsetSum,taken,subset,k,N,0,N-1)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

