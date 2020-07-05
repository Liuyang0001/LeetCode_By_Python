#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] wildcard-matching
#
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @functools.lru_cache(None)
        def dfs(i, j):
            if j == len(p): return i == len(s)
            if i < len(s) and s[i] == p[j] and dfs(i + 1, j + 1):
                return True
            if i < len(s) and p[j] == "?" and dfs(i + 1, j + 1): return True
            if p[j] == "*":
                # * 依次表示多个, 一个, 零个字符
                if (i < len(s) and (dfs(i + 1, j) or dfs(i + 1, j + 1))) or dfs(i, j + 1) : return True
            return False
        
        return dfs(0, 0)
# @lc code=end