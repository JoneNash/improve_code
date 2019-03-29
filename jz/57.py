#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/17 10:49
"""

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        root=pNode
        while(root.next):
            root=root.next

        self.result = []
        self.midTraversal(root)

        if self.result.index(pNode) != len(self.result) - 1 :
            return self.result[self.result.index(pNode)+1]
        else:
            return None



    def midTraversal(self,root):
        if not root:return
        self.midTraversal(self.left)
        self.result.append(root.val)
        self.midTraversal(self.left)



