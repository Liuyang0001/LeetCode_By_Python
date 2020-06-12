#
# @lc app=leetcode.cn id=1548 lang=python3
#
# [1548] check-if-all-1s-are-at-least-length-k-places-away
#
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        for i, e in enumerate(nums):
            # print(i,e)
            if e==0: continue
            if e == 1 and (last == None or i - last > k):
                # print(i)
                last = i
            else:
                return False
        return True
# @lc code=end