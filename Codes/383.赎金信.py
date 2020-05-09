#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
import itertools
from collections import Counter
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # s1 = set(itertools.permutations(ransomNote, 1))
        # s2 = set(itertools.permutations(magazine, 1))
        # return s2.union(s1)==s2
        c1, c2 = Counter(ransomNote), Counter(magazine)
        for k,val in c1.items():
            if k in c2 and val <= c2[k]:
                continue
            return False
        return True
# @lc code=end

