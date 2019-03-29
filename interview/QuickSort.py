#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/21 22:07
【贝壳】2.快排


参考解释：https://blog.csdn.net/tizzzzzz/article/details/79610375
"""

class Solution:
    def QuickSort(self,arr,start,end):
        if start<end:
            i=start
            j=end
            print "start,end: ",i,j
            base =arr[i]

            while i<j:

                #以下两个while循环
                # 第一个循环固定左侧游标i，右侧游标j从右端左移，碰到第一个符合条件的元素，将元素赋值到i元素
                # 右侧游标j固定，左侧游标i右移，碰到第一个符合条件的元素，将元素赋值到j元素
                while i<j  and base <=arr[j]:
                    j=j-1
                arr[i]=arr[j]

                while i<j  and arr[i] <=base:
                    i=i+1
                arr[j]=arr[i]
            #最后一个挖空的坑位，赋值base。如此，base左侧均小于等base，右侧均大于等于base
            # 另外，因为i、j每次相向移动一次，此时i=j
            arr[i]=base


            #分解开来，对左侧和右侧分别快排
            self.QuickSort(arr,start,i-1)
            self.QuickSort(arr, i+1,end)

            return
        else:
            return

    #扩展：堆排序
    # def HeapSort(self,arr)





if __name__ == '__main__':
    s=Solution()
    arr=[49,38,65,97,76,13,27,49]
    s.QuickSort(arr,0,len(arr)-1)

    print arr

