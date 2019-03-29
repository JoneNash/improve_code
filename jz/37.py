#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/20 09:36
"""

class Solution:
    def GetNumberOfK(self,array,k):
        if not array:
            return 0

        start=0
        end=len(array)-1
        count=0

        while(start<end):

            mid=(start+end)/2
            if(array[mid]>k):
                end =mid
            elif(array[mid]<k):
                start=mid
            else:
                tmp=mid
                while mid >=start and array[mid]==k:
                    count+=1
                    mid-=1
                mid = tmp+1
                while mid <=end and array[mid]==k:
                    count+=1
                    mid+=1
                return count
        return count


if __name__ == '__main__':
    array=[1,2,3,4,5,5,5,5,5,7,8,9]
    array = [1, 2, 3, 4, 5, 5, 5, 5, 5]
    array = [ 5, 5, 5, 5, 5,6,7,8,9]
    s=Solution()
    print s.GetNumberOfK(array,5)
