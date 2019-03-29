#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/11 15:12
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):

        res=[]

        if root is None:
            return False
        treePath=self.dfs(root)

        for path in treePath:
            if(sum(map(int,path.split("->"))) == expectNumber):
                res.append(map(int,path.split("->")))
        return res



    def dfs(self, root):
        if root is None:
            return []
        if root.left is  None and root.right is None:
            return [str(root.val)]

        treePath=[str(root.val)+"->"+ path for path in self.dfs(root.left)]
        treePath=treePath+[str(root.val)+"->"+ path for path in self.dfs(root.right)]

        return treePath


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)

    t1.right.left = TreeNode(0)
    t1.right.right = TreeNode(1)

    t1.right.left.left = TreeNode(4)

    print Solution().FindPath(t1,8)
