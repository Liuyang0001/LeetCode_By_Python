#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#
from typing import List
# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+ 1):
            cnt = 0
            while i > 0:
                # 按位与取最后一位
                if i & 1: cnt += 1
                i >>= 1
            res.append(cnt)
        return res
# @lc code=end
# 动态规划解法
# i为奇数 dp[i] = dp[i−1]+1
# i为偶数 dp[i] = dp[i // 2]

# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         dp=[0]*(num+1)
#         for i in range(1,num+1):
#             if(i%2==1):
#                 dp[i]=dp[i-1]+1
#             else:
#                 dp[i]=dp[i//2]
#         return dp