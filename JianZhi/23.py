#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/11 11:37
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here

        if(len(sequence)==0):
            return False

        root = sequence[-1]

        for i in range(len(sequence)) :
            print 'i: ',i
            if sequence[i]>root:
                break
        for j in    range(i,len(sequence)):
            print 'j: ', j
            if sequence[j]<root:
                return False

        left=True
        right=True
        if i>0:
            left = self.VerifySquenceOfBST(sequence[0:i])
        if i<len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i:-1])

        return left and right






if __name__ == '__main__':
    # seq=[2,4,3,7,9,8,5]
    seq = [7,6,5,3,4]

    print Solution().VerifySquenceOfBST(seq)