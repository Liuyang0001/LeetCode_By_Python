#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] word-break
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        if not wordDict: return not s
        # 找最长单词的长度
        max_len = max(map(len, wordDict)) 

        @functools.lru_cache(None)
        def helper(s):
            # 递归终止条件
            if not s:
                return True
            for i in range(len(s)):
                # 判断是否满足条件
                if i < max_len and s[:i+1] in wordDict and helper(s[i+1:]):
                    return True
            return False

        return helper(s)
# @lc code=end