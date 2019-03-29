#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/11 16:19
"""

# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None

        #第一步，复制Node
        dummy = pHead #dummy为起到"指针"的作用
        while dummy:
            dummyNext=dummy.next
            dummyCopy=RandomListNode(dummy.label)
            dummy.next=dummyCopy
            dummyCopy.next=dummyNext
            dummy=dummyNext

        #第二步，复制random连接
        dummy = pHead
        while dummy:
            dummyRandom=dummy.random
            if dummyRandom is not None:
                dummy.next.random=dummyRandom.next
            dummy=dummy.next.next

        #第三步，拆解

        dummy=pHead
        dummyCopy=pHead.next

        while dummy:
            copyNode=dummy.next
            dummyNext=copyNode.next
            dummy.next=dummyNext

            if dummyNext is not None:
                copyNode.next=dummyNext.next
            else:
                copyNode.next =None

            dummy=dummyNext

        return dummyCopy

if __name__ == '__main__':
    head=RandomListNode(1)
    n2=RandomListNode(2)
    n3= RandomListNode(3)
    n4 = RandomListNode(4)

    head.next=n2
    head.random=n3
    n2.next=n3
    n2.random=n4

    print Solution().Clone(head).next.label