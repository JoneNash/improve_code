#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/9 20:12
"""


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if((len(pushV) <> len(popV)) or (len(pushV)==0)):
            return False

        #用数组模拟栈
        arr=[]

        #模拟压栈
        while pushV:
            arr.append(pushV.pop(0))
            #如果模拟栈尾部元素与出栈数组头部元素相同
            if arr[-1] == popV[0]:
                arr.pop()
                popV.pop(0)
        #如果模拟栈与出栈都不为空时
        while arr and popV :
            print "@@"
            if arr[-1] == popV[0]:
                arr.pop()
                popV.pop(0)
            else:
                return False

        return True



if __name__ == '__main__':
    pushV = [1,2,3,4]
    popV = [1,4,3,2]

    # pushV =[1, 2, 3, 4, 5]
    # popV =[4, 5, 3, 2, 1]

    print Solution().IsPopOrder(pushV, popV)