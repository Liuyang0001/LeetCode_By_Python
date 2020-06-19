#
# @lc app=leetcode.cn id=1605 lang=python3
#
# [1605] minimum-number-of-days-to-make-m-bouquets
#
import numpy as np
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # if m==0 or k==0: return 0
        n = len(bloomDay)
        if m*k>n: return -1
        elif m*k==n: return max(bloomDay)
        # tem = bloomDay
        
        def check(day):
            a = [True if v <= day else False for v in bloomDay]
            count = 0
            n = len(bloomDay)
            s, t = 0, 0
            while t < n:
                if not a[t]:
                    count += (t-s) // k
                    s = t + 1
                t += 1
            count += (t-s) // k
            return count >= m
        
        c = set(bloomDay)
        c = sorted(c)
        # print(c)
        l=0
        r=len(c)-1
        while l<r:
            mid = (l+r)//2
            flag = check(c[mid])
            if flag:
                r = mid
            else:
                l = mid+1
        return c[r]
            
# @lc code=end