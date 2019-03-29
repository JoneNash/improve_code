#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/24 09:57
360：在一个非递减排序数组中，找到第一个匹配元素的下标
"""

class Solution:
    def FindFirstIndex(self,array,element):
        start=0
        end=len(array)-1
        index=end
        while start<end:
            print start,end
            #向下取整
            mid=(start+end)/2

            if array[mid]>element:
                end=mid-1
            elif array[mid]<element:
                start=mid+1
            else:
                end=mid
                if index>mid:
                    index=mid
        if array[index] == element:
            return index
        else:
            return -1


    # 延伸：找到最后一个匹配元素的index
    def FindLastIndex(self,array,element):
        start=0
        end=len(array)-1
        index=start
        while start<=end:
            print start,end
            #向下取整
            mid=(start+end)/2

            if array[mid]>element:
                end=mid-1
            elif array[mid]<element:
                start=mid+1
            else:
                start=mid+1
                if index<mid:
                    index=mid

        if array[index] == element:
            return index
        else:
            return -1
    


if __name__ == '__main__':
    s=Solution()
    print s.FindFirstIndex([1, 2, 3, 4, 5, 5, 5, 5, 5],5)
    print s.FindLastIndex([1, 2, 3, 4, 5, 5, 5, 5, 5],5)


