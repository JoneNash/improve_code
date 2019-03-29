#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/7 19:41
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here

        if pHead1 == None:
            return pHead2
        elif pHead2 == None:
            return pHead1
        else:


            l_merge=ListNode(0)
            tmp=l_merge
            while(pHead1 is not None and pHead2 is not None):
                if(pHead1.val>=pHead2.val):
                    tmp.next=pHead2
                    pHead2=pHead2.next
                else:
                    tmp.next = pHead1
                    pHead1 = pHead1.next
                tmp=tmp.next
            if(pHead1 is not None):
                tmp.next=pHead1
            else:
                tmp.next=pHead2

            return l_merge.next




if __name__ == '__main__':
    l1=ListNode(1)
    l1.next=ListNode(3)
    l1.next.next=ListNode(5)

    l2=ListNode(2)
    l2.next=ListNode(4)
    l2.next.next=ListNode(6)

    l_merge=Solution().Merge(l1,l2)

    print l_merge.val