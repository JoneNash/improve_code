#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/4 15:56

https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e?tpId=13&tqId=11154&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
解题思路：从左下角开始判断，如果target偏大，向右移动；如果target偏小，向上移动


"""

def Find(target,array):
    size_1=len(array)
    size_2=len(array[0])

    print size_1,size_2

    i=size_1-1
    j=0

    while(i>=0 and j<=size_2-1):
        print i,j
        if(target<array[i][j]):
            i=i-1
        elif (target>array[i][j]):
            j=j+1
        else:
            print "i:",i," j:",j
            return True
    return False



if __name__ == '__main__':
    arrays=[[1,2,3,4,5,6],
          [3,4,5,6,7,8],
          [4,5,7,8,9,10],
          [7,8,9,10,11,12]]

    # print Find(5, arrays)


    arrays=[[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]

    print Find(16,arrays)


