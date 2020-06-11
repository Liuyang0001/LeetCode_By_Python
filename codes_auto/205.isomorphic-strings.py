#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] isomorphic-strings
#
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 同构代表两个字符串中,
        # 每个位置上字符在自身第一次出现的索引相同
        return [*map(s.index,s)]==[*map(t.index,t)]
# @lc code=end