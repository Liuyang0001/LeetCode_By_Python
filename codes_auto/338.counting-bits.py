#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] counting-bits
#
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+ 1):
            # print(i)
            cnt = 0
            while i > 0:
                # print(i)
                if i & 1: cnt += 1
                i >>= 1
            res.append(cnt)
        return res
# @lc code=end