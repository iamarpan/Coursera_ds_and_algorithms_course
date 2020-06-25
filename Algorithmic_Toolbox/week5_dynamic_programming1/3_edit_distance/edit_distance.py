# Uses python3
def edit_distance(s, t):
    #write your code here
    cache = [[0 for b in range(len(s)+1)] for a in range(len(t)+1)]
    for i in range(len(t)+1):
        for j in range(len(s)+1):
            if(j==0):
                cache[i][j]=i
            elif(i==0):
                cache[i][j]=j
            else:
                if(s[j-1] == t[i-1]):
                    cache[i][j] = cache[i-1][j-1]
                else:
                    cache[i][j] = 1+min(cache[i-1][j],cache[i-1][j-1],cache[i][j-1])
    return cache[len(t)][len(s)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
