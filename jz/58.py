#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/17 11:00
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot is None: return True
        return self.comTree(pRoot.left,pRoot.right)

    def comTree(self,left,right):
        if(left is None ):return right is None
        if(right is None):return False
        if(left.val == right.val):
            return self.comTree(left.right,right.left) \
                   and self.comTree(left.left,right.right)
        else:
            return False


