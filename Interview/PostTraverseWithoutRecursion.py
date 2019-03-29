#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/21 16:57
【贝壳】1.二叉树后序非递归遍历
解题思路：
求解后序非递归遍历，即左->右->中的顺序。
解决非递归遍历问题，首先想到用栈。
这里采用两个栈，并初始化Root入栈1.
栈1出栈，按照左、右入栈，栈1出栈元素的val入栈2
栈1出栈，按照右左、右右入栈，栈1出栈元素的val入栈2

1）按照上面这种方式，会先访问当前节点，然后访问右节点，访问完右侧元素，开始依次向上访问左侧，至到遍历完根节点所有右侧节点
2）之后，采用相同的套路访问左节点

访问后的节点写入栈2，顺序为 根节点->右节点->左节点，最后，只需要依次出栈就可以转为:左节点->右节点->根节点

参考：  https://www.cnblogs.com/icekx/p/9127569.html


"""
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:

    # 后序打印二叉树（非递归）
    # 后序遍历为（左子树遍历结果——>右子树遍历结果——>根节点）的顺序，左子树和右子树又可以各自拆解。
    # 因为暂存各个阶段的根节点比较麻烦，所以，要转换一下思路，把后序遍历看做（根节点——>右子树遍历结果——>左子树遍历结果）的逆序
    # 根据这个思路，可以采用栈结构，每次从栈中读取一个节点，并将左子节点和右子节点依次入栈，然后以此类推，直到栈为空。这样就可以起到一次遍历（根节点——>右子树遍历结果——>左子树遍历结果）的效果
    # 最后，对结果数组逆序排列即可返回
    def PostOrderTraverse(self,Root):
        res=[]

        stack1=[]
        stack2=[]

        stack1.append(Root)

        while len(stack1)>0:
            node=stack1.pop()

            if node.left is not None:
                stack1.append(node.left)
            if node.right  is not None:
                stack1.append(node.right)

            stack2.append(node)

        while len(stack2)>0:
            res.append(stack2.pop().val)

        return res

    #第二种方式
    #整体思路和第一种方法类似，都是把后序遍历看做（根节点——>右子树遍历结果——>左子树遍历结果）的逆序
    #可以参照中序排列中利用节点是否为None来作为判断是否出栈的依据。
    #方法参考：https://www.cnblogs.com/qiaojushuang/p/7887517.html
    def PostOrderT(self,Root):
        res=[]
        stack=[]
        pos = Root
        while pos is not None or len(stack)>0:
            while pos is not None:
                res.append(pos.val)
                stack.append(pos)
                pos=pos.right
            if len(stack)>0:
                top=stack.pop()
                pos=top.left
        return res[::-1]


    #拓展：先序遍历
    def PreOrderTraverse(self,Root):
        res=[]
        stack=[]
        stack.append(Root)
        while  len(stack)>0:
            node=stack.pop()
            res.append(node.val)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return  res

    #拓展：中序遍历

    def InOrderTraverse(self,Root):
        res=[]
        stack=[]
        pos=Root

        while pos is not None or len(stack)>0:
            if pos is not None:
                stack.append(pos)
                pos=pos.left
            else:
                pos=stack.pop()
                res.append(pos.val)
                pos=pos.right
        return res





if __name__ == '__main__':

    Root=TreeNode(0)
    node1=TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    Root.left=node1
    Root.right = node4
    node1.left=node2
    node1.right=node3


    s=Solution()
    print s.PostOrderTraverse(Root)
    print s.PostOrderT(Root)
    print s.PreOrderTraverse(Root)
    print s.InOrderTraverse(Root)

