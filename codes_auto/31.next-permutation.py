#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] next-permutation
#
class Solution:


    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 初始化两个索引值
        firstIndex, secondIndex = -1, -1
        n = len(nums)
        # 找第一个最大索引
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                firstIndex = i
                break
        # 未找到则反转整个数组
        if firstIndex == -1:
            # 使用注释掉的代码效果一致
            # nums[:]为使得nums的地址不变
            nums[:]=nums[::-1]
            return 
        # 找第二个索引
        for i in range(n-1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        nums[:]= nums[:firstIndex+1]+nums[firstIndex+1:][::-1]
        # self.reverse(nums, firstIndex+1, n-1)
# @lc code=end