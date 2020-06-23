#
# @lc app=leetcode.cn id=100348 lang=python3
#
# [100348] permutation-ii-lcci
#
class Solution:
    def permutation(self, S: str) -> List[str]:
        s = sorted(S)
        # print(s)
        n = len(s)
        if n==0: return []
        if n==1: return [S]
        res = []
        def backtrack(tem:str,rest:List[str]):
            # print(rest)
            if len(tem)==n:
                res.append(tem)
                return
            for i in range(len(rest)):
                if i>0 and rest[i]==rest[i-1]:
                    continue
                backtrack(tem+rest[i], rest[:i]+rest[i+1:])
        backtrack("",s)
        return res
# @lc code=end