'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]

示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


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
