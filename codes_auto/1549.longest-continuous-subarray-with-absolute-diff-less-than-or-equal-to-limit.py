#
# @lc app=leetcode.cn id=1549 lang=python3
#
# [1549] longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit
#
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = j = 0
        st = []
        ans = 0
        while j < len(nums):
            bisect.insort(st, nums[j])
            while st[-1] - st[0] > limit:
                st.remove(nums[i])
                i += 1
            j += 1
            ans = max(ans, len(st))
        return ans
        
# @lc code=end