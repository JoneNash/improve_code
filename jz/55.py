#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/10 21:53
"""


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow,fast=pHead
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                slow2=pHead
                while(slow != slow2):
                    slow=slow.next
                    slow2=slow2.next

                return slow
        return None



if __name__ == '__main__':
    s = Solution()
