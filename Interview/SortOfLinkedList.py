#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/28 23:13
【快手？】
双向链表排序
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。避免最坏时间复杂度是O(n^2)。
以下采用归并排序。

代码参考：https://blog.csdn.net/qq_34364995/article/details/80994110
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.pre = None
        self.next = None

class Solution:

    #整体采用递归的归并

    #包含"分"的逻辑
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        mid = self.get_mid(head)
        l = head
        r = mid.next
        #l和r截断
        mid.next = None
        r.pre = None


        return self.merge(self.sortList(l), self.sortList(r))

    #"合"的逻辑
    def merge(self, p, q):
            tmp = ListNode(0)
            h = tmp
            while p and q:
                if p.val < q.val:
                    h.next = p
                    p.pre = h
                    p = p.next
                else:
                    h.next = q
                    q.pre=h
                    q = q.next
                h = h.next
            if p:
                h.next = p
                p.pre=h
            if q:
                h.next = q
                q.pre=h
            return tmp.next

    def get_mid(self, node):
        if node is None:
            return node
        fast = slow = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':
    n1=ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)


    head=ListNode(-1)
    head.next=n4
    n4.pre=head
    n4.next=n3
    n3.pre = n4
    n3.next = n2
    n2.pre = n3
    n2.next = n1
    n1.pre = n2



    s=Solution()
    s.sortList(head)

    print head.next.next.pre.val

