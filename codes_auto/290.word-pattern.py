#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] word-pattern
#
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split(" ")
        dic = collections.defaultdict(str)
        if len(pattern) != len(ls) or \
            len(set(pattern)) != len(set(ls)): return False
        for i in range(len(ls)):
            if not dic[pattern[i]]:
                dic[pattern[i]] = ls[i]
            elif dic[pattern[i]] != ls[i]:
                return False
        return True
# @lc code=end