#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2018/12/9 4:39 PM
"""

def reverse(x):
    prefix=1
    if x<0 :
        prefix=-1

    tmp=0
    s=abs(x)

    while s>0:
        tmp=tmp*10+s%10
        s=s/10
    print prefix*tmp
    if prefix*tmp >=-2**31 and prefix*tmp <=2**31-1  :
        return prefix*tmp
    else:
        return 0





if __name__ == '__main__':
    s=-1010
    print reverse(s)