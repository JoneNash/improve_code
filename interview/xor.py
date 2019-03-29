#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/13 10:34
【头条】
首先：位运算中异或的性质：两个相同数字异或=0，一个数和0异或还是它本身。

当只有一个数出现一次时，我们把数组中所有的数，依次异或运算，最后剩下的就是落单的数，因为成对儿出现的都抵消了。

依照这个思路，我们来看两个数（我们假设是AB）出现一次的数组。
我们首先还是先异或，剩下的数字肯定是A、B异或的结果，这个结果的二进制中的1，表现的是A和B的不同的位。
我们就取第一个1所在的位数，假设是第3位，接着把原数组分成两组，分组标准是第3位是否为1。
如此，相同的数肯定在一个组，因为相同数字所有位都相同，而不同的数，肯定不在一组。
然后把这两个组按照最开始的思路，依次异或，剩余的两个结果就是这两个只出现一次的数字。
"""

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        xor=0
        for i in array:
            xor=xor^i

        num1=0
        num2=0

        mask=1
        #mask标记特殊位，mask在特殊位为1
        while xor & mask ==0:
            mask <<=1

        for j in array:
            #按照特殊位是否为1来划分，等于0，j的特殊位为0
            if j & mask ==0:
                num1=num1^j
            #否则，j的特殊位为1
            else:
                num2^=j
        return [num1,num2]


##只有一个出现1次，其他都出现3次

    def FindNumsAppearOnceexceptionTriple(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            cnt = 0
            mask = 1 << i
            for num in nums:
                if num & mask:
                    cnt += 1
            if cnt % 3 == 1:
                res |= mask
        if res >= 2 ** 31:
            res -= 2 ** 32
        return res




if __name__ == '__main__':
    print Solution().FindNumsAppearOnce([1,2,3,5,7,1,2,3])

    print Solution().FindNumsAppearOnceexceptionTriple([1, 2, 3, -5, 1, 2, 3,1, 2, 3])