#
# @lc app=leetcode.cn id=1560 lang=python3
#
# [1560] number-of-students-doing-homework-at-a-given-time
#
class Solution:
    def busyStudent(self, s: List[int], e: List[int], q: int) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            if s[i]<=q<=e[i]:
                res+=1
        return res
# @lc code=end