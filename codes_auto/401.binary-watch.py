#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] binary-watch
#
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        for i in range(12):
            for j in range(60):
                if num == bin(i).count('1') + bin(j).count('1'):
                    yield "%d:%02d"%(i, j)
        # return list("%d:%02d"%(i, j) for j in range(60) for i in range(12) if num == bin(i).count('1') + bin(j).count('1'))
# @lc code=end