#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/11/27 12:37 PM
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


#递归
def addTwoNumbers_1( l1, l2, c=0):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    val = l1.val + l2.val + c
    #向下取整除法
    c = val // 10
    #取余
    ret = ListNode(val % 10)

    if (l1.next != None or l2.next != None or c != 0):
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        ret.next = addTwoNumbers_1(l1.next, l2.next, c)
    return ret

def addTwoNumbers_2( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    val = l1.val + l2.val
    c = val // 10
    ret = ListNode(val % 10)

    if (l1.next != None or l2.next != None or c != 0):
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        l2.next.val = l2.next.val + c
        ret.next = addTwoNumbers_2(l1.next, l2.next)
    return ret

def addTwoNumbers_3( l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None:
        return l2
    elif l2 == None:
        return l1

    remain = 0
    l = ListNode(None)
    result = l

    while l1 != None or l2 != None:
        if l1 == None:
            l1 = ListNode(0)
        elif l2 == None:
            l2 = ListNode(0)
        total = l1.val + l2.val + remain
        if total >= 10:
            total = total - 10
            remain = 1
        else:
            remain = 0
        l.next = ListNode(total)
        l1 = l1.next
        l2 = l2.next
        l = l.next
        print l.val


    if remain == 1:
        l.next = ListNode(remain)

    return result.next



if __name__ == '__main__':
    l1=ListNode(2)
    l1.next=ListNode(4)
    l1.next.next=ListNode(3)

    l2=ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # l_sum=addTwoNumbers_1(l1,l2, c=0)
    # l_sum =addTwoNumbers_2(l1,l2)
    l_sum = addTwoNumbers_3(l1, l2)


    print l_sum.val
    print l_sum.next.val
    print l_sum.next.next.val



