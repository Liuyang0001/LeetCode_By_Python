#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] find-first-and-last-position-of-element-in-sorted-array
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        if nums_len == 0:
            return [-1, -1]
        return [self.getLeft(nums, 0,  nums_len-1, target), self.getRight(nums, 0, nums_len-1, target)]

    # 寻找左边界
    def getLeft(self, nums: List[int], left: int, right: int, target: int) -> int:
        # 递归出口
        if left >= right:
            return left if nums[left] == target else - 1

        mid = (left + right) // 2

        if nums[mid] == target and nums[mid-1] != target:
            return mid
        # 递归入口
        if nums[mid] < target:
            return self.getLeft(nums, mid+1, right, target)
        elif nums[mid] >= target:  # mid==target时取左侧，向左递归
            return self.getLeft(nums, left, mid-1, target)

    # 寻找右边界
    def getRight(self, nums: List[int], left: int, right: int, target: int) -> int:
        if left >= right:
            return left if nums[left] == target else - 1

        mid = (left + right) // 2

        if nums[mid] == target and nums[mid+1] != target:
            return mid

        if nums[mid] > target:
            return self.getRight(nums, left, mid-1, target)
        elif nums[mid] <= target:  # mid==target时取右侧，向右递归
            return self.getRight(nums, mid+1, right, target)

# @lc code=end