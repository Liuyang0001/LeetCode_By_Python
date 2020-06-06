#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#
from typing import List
# @lc code=start
class Solution:
    def quick_pow(self, x, n, m):
        ans = 1
        while n > 0:
            if n & 1 == 1:
                ans = ans * x % m
            x = x * x % m     
            n >>= 1
        return ans    
        
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        for i in b:
            res = self.quick_pow(res, 10, 1337) * self.quick_pow(a, i, 1337)
        return res % 1337
# @lc code=end
# 直接调用函数即可
# class Solution:
#     def superPow(self, a: int, b: List[int]) -> int:
#         b = "".join(map(str,b))
#         return pow(a,int(b),1337)