# python3
import time
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))




def get_occurrences(pattern, text):
    M=len(pattern)
    N = len(text)
    i=0
    j=0
    p=0
    t=0
    h=1
    d = 256
    q=1000000007
    result =[]
    hashes =[None]*(N-M+1)
    for i in range(M-1):
        h = (h*d)%q
    for i in range(M):
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    hashes[0]=t
    for i in range(N-M):
        t = (d*(t-ord(text[i])*h) + ord(text[i+M]))%q
        hashes[i+1]=t
    for a in range(N-M+1):
        if(hashes[a]==p):
            if(text[a:len(pattern)+a]==pattern):
                result.append(a)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
