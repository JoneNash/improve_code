#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/1/10 11:21

挖坑+分治
"""

def QuickSort(myList,start,end):
    if start < end:
        i,j = start,end

        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        #递归前后半区
        print i,j
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)
    return myList


myList = [49,38,65,97,76,13,27,49]
print("Quick Sort: ")
QuickSort(myList,0,len(myList)-1)
print(myList)