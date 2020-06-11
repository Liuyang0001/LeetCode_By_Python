#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] minimum-number-of-frogs-croaking
#
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        s = 'croak'
        dic = {i:0 for i in s}
        ans = -1
        for i in croakOfFrogs:
            dic[i]+=1
            if any(dic[s[i+1]]>dic[s[i]] for i in range(len(s)-1)):
                return -1
            ans = max(ans,dic[s[0]])
            if dic[s[-1]]==1:
                for i in s:
                    dic[i]-=1
        return -1 if dic[s[0]] else ans
# @lc code=end