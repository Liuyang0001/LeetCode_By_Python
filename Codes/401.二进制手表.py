#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
from typing import List
# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        for i in range(12):
            for j in range(60):
                if num == bin(i).count('1') + bin(j).count('1'):
                    yield "%d:%02d"%(i, j)
# @lc code=end
# 一行解法
# return list("%d:%02d"%(i, j) for j in range(60) for i in range(12) if num == bin(i).count('1') + bin(j).count('1'))