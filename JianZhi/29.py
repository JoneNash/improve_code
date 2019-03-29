#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/13 21:22
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if(k>len(tinput)):
            return []


        arr=self.qucik_sort(tinput,0,len(tinput)-1)


        return arr[:k]




    def qucik_sort(self,input,start,end):
        if start<end:
            i,j=start,end

            base=input[i]

            while i<j :
                while(i<j and input[j]>=base):
                    j=j-1

                input[i]=input[j]

                while(i<j and input[i]<=base):
                    i=i+1

                input[j]=input[i]

            input[j]=base

            self.qucik_sort(input, start, i - 1)
            self.qucik_sort(input, i +1,end)


        return input





if __name__ == '__main__':
    input=[1,8,3,5,2,0,9,12,5,6,3,9]

    print Solution().GetLeastNumbers_Solution(input,6)