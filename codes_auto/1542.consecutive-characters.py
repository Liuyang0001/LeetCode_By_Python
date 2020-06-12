#
# @lc app=leetcode.cn id=1542 lang=python3
#
# [1542] consecutive-characters
#
class Solution:
    def maxPower(self, s: str) -> int:
        if not s: return 0
        cnt,res = 1,1
        for i in range(1,len(s)):
            if s[i]==s[i-1]: cnt+=1
            else: cnt = 1
            res = max(res,cnt)
                
        return res
# @lc code=end