#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] repeated-dna-sequences
#
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res, visted = set(), set()
        n = len(s)
        for i in range(n - 9):
            tem = s[i:i + 10]
            if tem in visted:
                res.add(tem)
            visted.add(tem)
        return list(res)
# @lc code=end