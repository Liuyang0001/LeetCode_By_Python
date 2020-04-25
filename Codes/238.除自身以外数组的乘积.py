#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        tem = 1
        # res[i]存着i左侧的乘积
        for i in range(n):
            res[i] = tem
            tem = tem * nums[i]
        # print(nums,res)
        tem = 1
        # tem存着i右侧的乘积值
        # 左侧×右侧= res[i]
        for i in range(n - 1, -1, -1):
            res[i] *= tem
            tem *= nums[i]
        return res

# @lc code=end

