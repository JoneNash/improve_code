#!/usr/bin/env python
# encoding: utf-8

"""
@author: leidelong
@contact: leidl8907@gmail.com
@time: 2019/2/1 14:31

https://www.cnblogs.com/strengthen/p/10326127.html
"""

def mincostTickets( days, costs):
    """
    :type days: List[int]
    :type costs: List[int]
    :rtype: int
    """
    day_idx = 0
    dp = [0] * (days[-1] + 1)

    for i in xrange(days[-1] + 1):
        if i == days[day_idx]:
            dp[i] = min(dp[i - 1] + costs[0], dp[max(i - 7, 0)] + costs[1], dp[max(i - 30, 0)] + costs[2])
            day_idx += 1
        else:
            dp[i] = dp[i - 1]

    return dp[-1]

if __name__ == '__main__':
    days=[1,4,7,8,9,10,18,80]
    costs=[2,10,20]

    print mincostTickets(days,costs)