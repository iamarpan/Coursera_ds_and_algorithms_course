#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def inOrderTraversal(tree,i=0,result=[]):
    if i!=-1:
        inOrderTraversal(tree,tree[i][1],result)
        result.append(tree[i][0])
        inOrderTraversal(tree,tree[i][2],result)
    if(len(result)==len(tree)):
        return result
    return

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
    result = inOrderTraversal(tree)
    if(len(result)<2):
        return True
    for a in range(1,len(result)):
        if(result[a]<result[a-1]):
            return False
    return True

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  if(nodes ==0):
      print("CORRECT")
      return
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
