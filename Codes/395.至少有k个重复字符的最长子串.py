#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#
from collections import Counter
# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s: return 0
        for key,val in Counter(s).items():
            if val < k:
                return max(self.longestSubstring(ss, k) for ss in s.split(key))
        return len(s)
# @lc code=end

