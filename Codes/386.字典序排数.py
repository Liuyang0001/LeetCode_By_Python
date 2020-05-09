#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
from typing import List
# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1,n+1),key=lambda x:str(x))
# @lc code=end

