#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/20 10:31
"""

class Solution:
    def IsBalanced_Solution(self, pRoot):
        def balance(node):
            if not node:
                return 0
            l = balance(node.left)
            r = balance(node.right)
            return -1 if l == -1 or r == -1 or abs(l - r) > 1 else max(l, r) + 1

        return balance(pRoot) != -1

