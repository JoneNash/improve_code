#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/17 10:35
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        stack1 = []
        stack2 = []

        tmp1 = pHead1
        tmp2 = pHead2

        while tmp1:
            stack1.append(tmp1)
            tmp1 = tmp1.next

        while tmp2:
            stack2.append(tmp2)
            tmp2 = tmp2.next

        sameNode = None
        while (stack1 and stack2):
            if (stack1[-1] == stack2[-1]):
                sameNode = stack1.pop()
                stack2.pop()
            else:
                break
        return sameNode



if __name__ == '__main__':
    h1=ListNode(1)
    h2=ListNode(2)

    h10=ListNode(10)
    h11 = ListNode(11)

    h12=ListNode(12)
    h13 = ListNode(13)

    h1.next=h2
    h2.next=h12

    h10.next=h11
    h11.next=h12
    h12.next=h13

    print Solution().FindFirstCommonNode(h1,h10).val

