#
# @lc app=leetcode.cn id=1524 lang=python3
#
# [1524] string-matching-in-an-array
#
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        if n==1: return []
        if n==2:
            if words[0] in words[1]: return [words[0]]
            elif words[i] in words[0]: return [words[1]]
            else: return []
        res = []
        for i in range(n):
            tem = "*".join(words[:i]+words[i+1:])
            if words[i] in tem:
                res.append(words[i])
        return res
# @lc code=end