#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/17 10:31
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        Head=ListNode(-1)
        Head.next=pHead
        p=Head
        last=Head.next


        while(last != None):
            if(last.next!=None and last.val == last.next.val):
                while(last.next!=None and last.val == last.next.val):
                    last=last.next
                p.next=last.next
                last=last.next
            else:
                p=p.next
                last=last.next
        return Head.next


