#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/7 20:32

https://www.nowcoder.com/questionTerminal/6e196c44c7004d15b1610b9afca8bd88

http://www.cnblogs.com/heyonggang/archive/2013/11/03/3405482.html
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def equal(self, pRoot1, pRoot2):
        # write code here
        if(pRoot2 is None): return  True
        if(pRoot1 is None): return False

        if(pRoot1.val == pRoot2.val):
            return self.equal(pRoot1.left,pRoot2.left) and self.equal(pRoot1.right,pRoot2.right)
        else:
            return False



    def HasSubtree(self, pRoot1, pRoot2):
        if(pRoot1 is None or pRoot2 is None ):
            return False
        return  self.equal(pRoot1,pRoot2) \
                or self.HasSubtree(pRoot1.left,pRoot2)\
                or self.HasSubtree(pRoot1.right,pRoot2)


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(4)
    t2.right = TreeNode(5)

    t1 = TreeNode(1)
    t2 = TreeNode(1)

    print Solution().HasSubtree(t1, t2)


