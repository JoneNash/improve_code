#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/10 21:20
"""

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here

        if(len(array)<2):
            return None

        low=0
        high=len(array)-1

        sum_list=[]

        while(low<high ):
            total_sum=array[low] + array[high]
            if(total_sum == tsum):
                return[array[low],array[high]]
            while(low<high and array[low] + array[high]>tsum): high=high-1
            while(low<high and array[low] + array[high]<tsum): low=low+1


if __name__ == '__main__':
    s=Solution()
    print s.FindNumbersWithSum(range(1,100,2),70)