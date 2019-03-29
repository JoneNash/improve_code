#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/13 20:33
"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here

        dict={}
        print len(numbers)
        for i in range(len(numbers)):
            print numbers[i]
            if  dict.has_key(numbers[i]):
                dict[numbers[i]]=dict.get(numbers[i])+1
            else:
                dict[numbers[i]] =1

        print dict.keys()
        for  i in dict.keys():
            print i,':',dict.get(i)
            if dict.get(i)>len(numbers)/2:
                return i
        return 0




if __name__ == '__main__':
    arr=[1,2,3,2,2,2,5,4,2]
    print Solution().MoreThanHalfNum_Solution(arr)