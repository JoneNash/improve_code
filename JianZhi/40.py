#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/20 14:28
"""

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        xor=0
        for i in array:
            xor=xor^i

        print xor
        num1=0
        num2=0

        mask=1
        #mask标记特殊位，mask在特殊位为1
        while xor & mask ==0:
            mask <<=1

        for j in array:
            #按照特殊位是否为1来划分，等于0，j的特殊位为0
            if j & mask ==0:
                num1=num1^j
            #否则，j的特殊位为1
            else:
                num2^=j
        return [num1,num2]

if __name__ == '__main__':
    s=Solution()
    print s.FindNumsAppearOnce([1,2,3,2,3,4])