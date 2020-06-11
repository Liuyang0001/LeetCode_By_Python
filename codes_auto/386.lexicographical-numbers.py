#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] lexicographical-numbers
#
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1,n+1),key=lambda x:str(x))
# @lc code=end