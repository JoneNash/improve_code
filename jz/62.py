#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/17 15:23
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.res=[]
        self.dfs(pRoot)

        return self.res[k-1] if 0<k<=len(self.res) else None

    def dfs(self,root):
        if not root:return
        self.dfs(root.left)
        self.res.append(root)
        self.dfs(root.right)

