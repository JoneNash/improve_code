#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/10 20:41
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        cursor_low=1
        cursor_high=2

        total_sum=0

        sum_list=[]

        while(cursor_low<cursor_high):
            print(cursor_low,cursor_high)
            total_sum=(cursor_low+cursor_high)*(cursor_high-cursor_low+1)/2

            if(total_sum==tsum):
                sum_list.append(range(cursor_low,cursor_high+1))
                cursor_low=cursor_low+1
            elif(total_sum<tsum):
                cursor_high=cursor_high+1
            else:
                cursor_low = cursor_low + 1

        return sum_list


if __name__ == '__main__':
    s=Solution()
    print s.FindContinuousSequence(100)
