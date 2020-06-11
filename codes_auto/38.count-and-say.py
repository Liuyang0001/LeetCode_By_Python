#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] count-and-say
#
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1: return "1"
        def helper(cur):
            nxt = ""
            cnt=1
            for i in range(1,len(cur)):
                if cur[i]!=cur[i-1]:
                    nxt+=(str(cnt)+str(cur[i-1]))
                    cnt=1
                else:
                    cnt+=1
            nxt+=(str(cnt)+str(cur[-1]))
            return nxt
        res ="1"
        while n>1:
            res = helper(res)
            # print(res)
            n-=1
        return res
        
# @lc code=end