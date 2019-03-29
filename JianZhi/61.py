#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/17 14:46
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.flag=-1


    def Serialize(self, root):
        # write code here
        if not root:
            return "#,"
        return str(root.val)+","+self.Serialize(root.left)+self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.flag+=1
        l=s.split(',')

        if(self.flag>=len(l)):
            return None
        root = None

        if l[self.flag] != '#':
            print self.flag
            root=TreeNode(int(l[self.flag]))
            root.left=self.Deserialize(s)
            root.right=self.Deserialize(s)
        return root


if __name__ == '__main__':
    t0=TreeNode(0)
    t0.left=TreeNode(-1)
    t0.right = TreeNode(1)

    s=Solution()
    strSer=s.Serialize(t0)
    print strSer
    t=s.Deserialize(strSer)