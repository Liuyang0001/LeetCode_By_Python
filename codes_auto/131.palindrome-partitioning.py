#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] palindrome-partitioning
#
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(tem,rest):
            if not rest:
                res.append(tem)
                return
            for i in range(1,len(rest)+1):
                if rest[:i]==rest[:i][::-1]:
                    backtrack(tem+[rest[:i]],rest[i:])
        backtrack([],s)
        return res    
# @lc code=end