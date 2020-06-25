# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,i=0,result=[]):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if i!=-1:
        self.inOrder(self.left[i],result)
        result.append(self.key[i])
        self.inOrder(self.right[i],result)
    if(len(result)==len(self.key)):
        return result
    return
                
  def preOrder(self,i=0,result=[]):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if i!=-1:
        result.append(self.key[i])
        self.preOrder(self.left[i],result)
        self.preOrder(self.right[i],result)
    if(len(result)==len(self.key)):
        return result
    return 
                

  def postOrder(self,i=0,result=[]):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if i!=-1:
        self.postOrder(self.left[i],result)
        self.postOrder(self.right[i],result)
        result.append(self.key[i])
    if(len(result)==len(self.key)):
        return result
    return
                

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
