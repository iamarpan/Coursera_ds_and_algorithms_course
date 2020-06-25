#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def isBST(j,mn,mx):
    if j not in tree:
        return True
    if(tree[j][0]<mn or tree[j][0]>mx): return False
    return isBST(tree[j][1],mn,tree[j][0]-1) and isBST(tree[j][2],tree[j][0],mx)

def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree,int_max,int_min = {},2147483647, -2147483648
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if isBST(0,int_min,int_max):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
