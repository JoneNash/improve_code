#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/4 16:22
https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode==None:
            return []
        else:
            return self.printListFromTailToHead(listNode.next)+[listNode.val]

if __name__ == '__main__':
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)

    print Solution().printListFromTailToHead(head)