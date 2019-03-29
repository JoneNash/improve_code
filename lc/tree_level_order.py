#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/1/23 15:40
"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x,left,right):
        self.val = x
        self.left = left
        self.right = right


    def levelOrder(self, ):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if self is None:
            return res

        #构建一个队列
        q=[self]

        while len(q)!=0:
            print q
            #用于记录节点的值
            res.append([node.val for node in q])
            #用来记录下一层node
            new_q=[]
            #按照当前层顺序（内部按照left、right顺序）访问，并写入队列
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q=new_q
            print 'len(q) :',len(q)

        return res


def construct_tree(pre_order, mid_order):
  #
  if len(pre_order) == 0 or len(mid_order) ==0 :
    return None
  # 前序遍历的第一个结点一定是根结点
  root_data = pre_order[0]
  for i in range(0, len(mid_order)):
    if mid_order[i] == root_data:
      break
  # 递归构造左子树和右子树
  left = construct_tree(pre_order[1 : 1 + i], mid_order[:i])
  right = construct_tree(pre_order[1 + i:], mid_order[i+1:])
  root=TreeNode(root_data, left, right)
  return root




if __name__ == '__main__':


    root = TreeNode('a',None,None)
    root_left=TreeNode('b',None,None)
    root_right = TreeNode('c',None,None)
    l_left=TreeNode('d',None,None)
    l_right=TreeNode('e',None,None)
    r_left = TreeNode('f',None,None)
    r_right = TreeNode('g',None,None)

    root.left=root_left
    root.right=root_right
    root_left.left=l_left
    root_left.right=l_right
    root_right.left=r_left
    root_right.right = r_right


    print root.levelOrder()


    print "@@@@@@"

    # pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    # mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
    # root2 = construct_tree(pre_order, mid_order)
    # print root2.levelOrder()