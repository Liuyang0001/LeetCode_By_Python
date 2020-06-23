#
# @lc app=leetcode.cn id=1000013 lang=python3
#
# [1000013] peaks-and-valleys-lcci
#
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2: return
        for i in range(1, n):
            # 奇数为谷，相同值无需处理
            if i%1 == 0 and nums[i-1] > nums[i]:  
                nums[i-1], nums[i] = nums[i], nums[i-1] # 交换
            # 偶数为峰，相同值无需处理
            if i%2 == 0 and nums[i-1] < nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1] # 交换
# @lc code=end