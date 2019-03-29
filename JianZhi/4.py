#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/4 16:37

https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6?tpId=13&tqId=11157&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking

采用递归方法

https://www.nowcoder.com/questionTerminal/8a19cbe657394eeaac2f6ea9b0f6fcf6
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if(len(pre)==0 or len(tin)==0):
            return None
        root=TreeNode(pre.pop(0))
        index=tin.index(root.val)
        root.left=self.reConstructBinaryTree(pre,tin[:index])
        root.right=self.reConstructBinaryTree(pre,tin[index+1:])

        return root

if __name__ == '__main__':
    pre_order=[1,2,4,5,3,6,7]
    middle_order=[4,2,5,1,6,3,7]

    tree=Solution().reConstructBinaryTree(pre_order,middle_order)


