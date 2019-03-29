#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/8 22:16
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Mirror(self, root):
        if root is None:
            return root

        tmp_left=root.left
        tmp_right=root.right

        root.left=self.Mirror(tmp_right)
        root.right=self.Mirror(tmp_left)

        return root



if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)

    t2=Solution().Mirror(t1)

    print t2.right.left.val


