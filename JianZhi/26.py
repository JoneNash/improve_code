#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/11 19:32
https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5?tpId=13&tqId=11179&tPage=2&rp=2&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:return None
        self.arr=[]
        self.MidTraverse(pRootOfTree)
        print len(self.arr)

        for i,v in enumerate(self.arr[:-1]):
            v.right=self.arr[i+1]
            self.arr[i + 1].left=v
        return self.arr[0]


    def MidTraverse(self,root):
        if(not root): return None
        self.MidTraverse(root.left)
        self.arr.append(root)
        self.MidTraverse(root.right)

if __name__ == '__main__':

    head=TreeNode(5)
    head.left=TreeNode(3)
    head.left.left = TreeNode(1)
    head.left.right = TreeNode(4)

    head.right=TreeNode(7)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(8)

    print Solution().Convert(head).val