#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/1/10 11:39
"""

def reverse_loop1(head):
    if head.next == None:
        return head
    new_head = reverse_loop1(head.next)
    head.next.next = head
    head.next = None
    return new_head

def reverse_loop2(head):
    p = head
    q = head.next
    p.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    return p
def reverse_loop3(head):
    p = head.next
    while p.next:
        q = p.next
        p.next = q.next
        head.next = q
        q.next = p

    p.next = head
    head = head.next
    p.next.next = None
    return head



#节点定义
class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#测试用例
if __name__ == '__main__':
    l1 = LNode(3)
    l1.next = LNode(2)
    l1.next.next = LNode(1)
    l1.next.next.next = LNode(99)
    l = reverse_loop1(l1)
    print l.val, l.next.val, l.next.next.val, l.next.next.next.val
