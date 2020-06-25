# Uses python3
import pdb;

def optimal_points(segments):
    segments.sort(key=lambda x:x[1])
    index = 0 
    coordinates = []
    n = len(segments)
    while index<n:
        curr = segments[index]
        while(index<n-1 and curr[1]>=segments[index+1][0]):
            index+=1
        coordinates.append(curr[1])
        index+=1
    return (len(coordinates),coordinates)



if __name__ == '__main__':
    n = int(input())
    segment = []
    for a in range(n):
        (a,b) = list(map(int,input().split()))
        segment.append((a,b))
    segment.sort()
    (visits,time) = optimal_points(segment)
    print(visits)
    print(" ".join([str(a)for a in time]))
