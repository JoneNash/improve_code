#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/6 16:31
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here

        arrs = []


        while head:
            arrs.append(head)
            head = head.next
        if(k>len(arrs) or k<=0):
            return None
        else:
            return arrs[-k]

if __name__ == '__main__':
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    print Solution().FindKthToTail(head,2)
