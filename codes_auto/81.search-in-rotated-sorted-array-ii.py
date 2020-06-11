#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] search-in-rotated-sorted-array-ii
#
# 库函数法
# from collections import Counter
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         nums_dict = Counter(nums)
#         if nums_dict[target] == 0:
#             return False
#         return True

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid, left, right = 0, 0, len(nums)-1
        while left <= right:  # 二分法
            mid = (left + right) // 2
            # 找到该点索引值
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            # 旋转点T在mid右区间
            # [left......mid....T....right]
            if nums[left] <= nums[mid]:
                # target在[left,mid)的升序空间中
                if nums[left] <= target < nums[mid]:
                    right = mid
                # target在(mid,T]或者[T,right]中
                else:
                    left = mid + 1
            # 旋转点T在mid左区间
            # [left...T...mid........right]
            elif nums[left] > nums[mid]:
                # target在(mid,right]的升序空间中
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # target在[left,T]或者[T，mid)
                else:
                    right = mid
        # 未找到该点
        return False
# @lc code=end