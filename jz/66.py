#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/18 14:25
"""

class Solution:

    def movingCount(self, threshold, rows, cols):
        # write code here
        self.dict = set()
        self.rows=rows
        self.cols=cols
        self.search(threshold,0,0)

        return len(self.dict)

    def judge(self,threshold,i,j):
        return sum(map(int,list(str(i))))+sum(map(int,list(str(j))))<=threshold


    def search(self,thre,i,j):
        if self.judge(thre,i,j) and (i,j) not in self.dict:
            self.dict.add((i,j))
            #向下移动
            if i<self.rows-1 :
                self.search(thre,i+1,j)
            if j<self.cols-1:
                self.search(thre, i , j+1)


if __name__ == '__main__':
    s=Solution()
    print s.movingCount(5,10,10)