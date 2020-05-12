#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#
import re
# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pat = ".*?"+"[a-z]*?".join([i for i in s])
        # print(pat)
        return True if re.match(pat,t) else False
# @lc code=end

