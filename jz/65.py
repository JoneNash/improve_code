#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/3/18 09:09
"""

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:return False
        if not path :return True

        mat=[list(matrix[i*cols:i*cols+cols])   for i in range(rows)  ]

        for i in range(rows):
            for j in range(cols):
                if  self.search(mat,i,j,path):
                    return True
        return False

    def search(self, matrix, i, j, p):

        if matrix[i][j] == p[0]:
            #p已读取完毕
            if not p[1:]:
                return True
            #1.读取后，当前位置赋值为空
            matrix[i][j]=''

            if i>0 and self.search(matrix,i-1,j,p[1:]):
                return True
            if i<len(matrix)-1 and self.search(matrix,i+1,j,p[1:]):
                return True
            if j>0 and self.search(matrix,i,j-1,p[1:]):
                return True
            if j<len(matrix[0])-1 and self.search(matrix,i,j+1,p[1:]):
                return True

            #2.匹配失败，还原取值
            matrix[i][j] = p[0]
            return False
        else:
            return False




if __name__ == '__main__':
    s=Solution()
    print s.hasPath("abcesfcsadee",3,4,"abcc")
    print s.hasPath("ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS", 5, 8, "SGGFIECVAASABCEHJIGQEM")
