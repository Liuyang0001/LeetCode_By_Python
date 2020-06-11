#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] count-primes
#
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3: return 0
        # 0,1不是质数
        out = [0]+[0]+[1]*(n-2)
        for i in range(2,int(n**0.5)+1):
            if out[i]==1:
                for j in range(i*i,n,i):
                    out[j]=0
        return sum(out)
        
# @lc code=end