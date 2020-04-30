#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
import bisect
from typing import List
# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        dp = [1] * n
        # dp状态i表示为到i为止有多少个递增子序列
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i]==3: return True
        return False

# @lc code=end
# class Solution:
    # def increasingTriplet(self, nums: List[int]) -> bool:
        # min_num,sec_num = float('inf'),float('inf')  # 初始化最小值，次小值
                                                     
        # for num in nums:                               
        #     min_num = min(num,min_num)                 # 维护min_num为最小值
        #     if num > min_num:                          # 找到了次小值
        #         sec_num = min(num,sec_num)             
        #     if num > sec_num:                          # 找到了第三大的数
        #         return True

        # return False