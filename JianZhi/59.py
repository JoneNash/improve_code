#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/17 11:17
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return

        stack=[pRoot]
        result=[]

        while stack:
            nextStack=[]
            res=[]

            for i in stack:
                res.append(i.val)
                if i.left:
                    nextStack.append(i.left)
                if i.right:
                    nextStack.append(i.right)
            stack=nextStack

            result.append(res)
        returnResult=[]

        for i,v in enumerate(result):
            if i%2==0:
                returnResult.append(v)
            else:
                returnResult.append(v[::-1])

        return returnResult





