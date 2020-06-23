#
# @lc app=leetcode.cn id=100161 lang=python3
#
# [100161] compress-string-lcci
#
class Solution:
    def compressString(self, S: str) -> str:
        res = ""
        count = 1
        n = len(S)
        if n==1 or n==0:
            return S
        for i in range(0,n-1):
            if count==1:
                res+=S[i]
            if S[i]==S[i+1]:
                count+=1
            else:
                res += str(count)
                count = 1
        if S[n-1]==S[n-2]:
            res = res+str(count)
        else:
            res = res+S[-1]+str(count)
        return res if len(res)<n else S
# @lc code=end