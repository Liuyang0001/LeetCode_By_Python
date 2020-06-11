#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] search-in-rotated-sorted-array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: return -1        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:  # [mid, r]有序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
            else:  # [l, mid]有序
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
        return -1 if nums[l] != target else l
# @lc code=end