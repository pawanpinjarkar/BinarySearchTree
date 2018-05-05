#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 23:18:01 2017

@author: pawan
Applied Algorithms
CSCI B505
Fall 2017
Programming Assignment 5
"""

class Node:
    #constructor of class
    def __init__(self,key): 
        self.key = key  #information for node
        self.left = None  #left leaf
        self.right = None #right leaf

class Sum:
    #constructor of class
    def __init__(self): 
        self.sum = 0

class BST:
    #constructor of class
    def __init__(self):
        self.root = None
    
    # Inserts item into the tree.
    def insert(self,item):
        if self.root == None:
            self.root = Node(item)
        else:
            current = self.root
            while 1:
                if item < current.key:
                    if current.left:
                        current = current.left
                    else:
                       current.left = Node(item)
                       break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(item)
                        break

     
        
    # Prints elements of the tree inorder.
    def printTree(self,node):
        if node is not None:
            self.printTree(node.left)
            print (node.key,end=' ')
            self.printTree(node.right)
            
    # Returns True if item is in the tree, otherwise False.
    def contains(self,k):
        current = self.root
        while(current!=None):
            if(current.key==k):
                return True
            elif(current.key>k):
                current = current.left
            else:
                current = current.right
        return False
    
    # Returns the number of nodes in the tree.
    def size(self,current):
        if current is None:
            return 0
        else:
            return self.size(current.left) +1+ self.size(current.right) 
        
    # Returns the smallest element in the tree.
    def smallest(self,current):
        if current is None:
            return 'Tree is empty'
        else:
            if current.left is None:
               return current.key
            else:
                return self.smallest(current.left)
            
    # Returns the largest element in the tree.
    def largest(self,current):
        if current is None:
            return 'Tree is empty'
        else:
            if current.right is None:
               return current.key
            else:
                return self.largest(current.right)
            
    # Transforms the tree such that each node contains sum of all
    # nodes greater than that node.
    def greaterSumTree(self,current,treeSum):
         if current is None:
             return 'Tree is empty' 
         self.greaterSumTree(current.right,treeSum)
         temp = treeSum.sum
         treeSum.sum = temp + current.key
         current.key = temp
         self.greaterSumTree(current.left,treeSum)
         
            
def main(array):
    # create new BST instance
    bst = BST() 
    for item in array:
        bst.insert(item)
    print ('Input :',array)
    print('\nDoes tree contain 500 ?',bst.contains(500))
    print('Does tree contain 2 ?',bst.contains(2))


    print('\nSize of tree =',bst.size(bst.root))
    
    print('The smallest element in the tree =',bst.smallest(bst.root))
    print('The largest element in the tree =',bst.largest(bst.root))
    
    print('\ncalling printTree() before calling greaterSumTree()')
    bst.printTree(bst.root)
    bst.greaterSumTree(bst.root,Sum())
    print('\n\ncalling printTree() after calling greaterSumTree()')
    bst.printTree(bst.root)
    
# Program execution starts here
array = [2,34,2,35,45,145,65,3,2,5,1,245,500]
main(array)
print('\n-----------------------------------------------------------------')
array = [5, 3, 9, 7, 1, 4, 0, 12, 11, 13, 15, 6, 2, 8, 10, 14]
main(array)