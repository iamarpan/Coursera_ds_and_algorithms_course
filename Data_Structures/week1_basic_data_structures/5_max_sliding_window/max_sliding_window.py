# python3
class Queue:
    def __init__(self,K):
        self.pushStack = []
        self.popStack = []
        self.K = K

    def enqueue(self,value):
        if(len(self.pushStack)==0):
            self.pushStack.append([value,value])
        elif(len(self.pushStack)>0 and not self.isFull()):
            if(value>=self.pushStack[-1][1]):
                self.pushStack.append([value,value])
            else:
                self.pushStack.append([value,self.pushStack[-1][1]])

        if(self.isFull()):
            while(len(self.pushStack)>0):
                val = self.pushStack.pop()
                if(len(self.popStack)==0):
                    element = [val[0],val[0]]
                    self.popStack.append(element)
                else:
                    element = (val[0],max(val[0],self.popStack[-1][1]))
                    self.popStack.append(element)


    def dequeue(self):
        if(len(self.pushStack)>0 and len(self.popStack)>0):
            val = self.popStack.pop()
            return max(self.pushStack[-1][1],val[1])
        elif(len(self.pushStack)==0):
            return self.popStack.pop()[1]

    def isFull(self):
        if(len(self.pushStack)==self.K):
            return True
        return False



def max_sliding_window_naive(sequence, m):
    queue = Queue(m)
    maximums = []
    for a in range(m):
        queue.enqueue(sequence[a])
    for i in range(m,len(sequence)+1):
        maximum = queue.dequeue()
        maximums.append(maximum)
        if(i<len(sequence)):
            queue.enqueue(sequence[i])
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window_naive(input_sequence, window_size))
