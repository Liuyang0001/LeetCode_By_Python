#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#
# 题目的意思是编写一个函数来查找子串，
# 这个子串长度为10，在原字符串中出现超过一次
# @lc code=start
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

