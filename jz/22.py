#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/11 11:21


"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]



    def PrintFromTopToBottom(self, root):
        # write code here
        if(root is None):
            return []

        arr = []
        arrNode = []

        arrNode.append(root)

        while arrNode:
            arr.append(arrNode[0].val)
            if(arrNode[0].left is not None):
                arrNode.append(arrNode[0].left)
            if (arrNode[0].right is not None):
                arrNode.append(arrNode[0].right)
            arrNode.pop(0)
        return arr





if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)

    print Solution().PrintFromTopToBottom(t1)
