#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        return len(s.split())
# @lc code=end

