#
# @lc app=leetcode.cn id=1543 lang=python3
#
# [1543] simplified-fractions
#
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n==1: return []
        res = []
        dic = set()
        for i in range(1,n+1):
            for j in range(1,i):
                if j/i not in dic:
                    dic.add(j/i)
                    res.append("{}/{}".format(j,i))
        return res
# @lc code=end