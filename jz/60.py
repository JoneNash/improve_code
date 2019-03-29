#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/17 11:33
"""


def Print(self, pRoot):
    # write code here
    if pRoot is None:
        return []

    stack = [pRoot]
    nextStack=[]
    result = []

    while stack:
        nextStack = []
        res = []

        for i in stack:
            res.append(i.val)
            if i.left:
                nextStack.append(i.left)
            if i.right:
                nextStack.append(i.right)
        stack = nextStack
        result.append(res)
    return result
