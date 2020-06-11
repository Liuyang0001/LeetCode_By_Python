#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] count-of-smaller-numbers-after-self
#
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        q = []
        res = []
        # 从后向前进行二分二分插入q中
        for num in nums[::-1]:
            # print(q)
            i = bisect.bisect_left(q,num)
            res.insert(0,i)
            q.insert(i,num)
        return res
# @lc code=end