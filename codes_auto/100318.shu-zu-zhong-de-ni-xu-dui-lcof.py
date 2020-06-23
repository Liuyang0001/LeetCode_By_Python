#
# @lc app=leetcode.cn id=100318 lang=python3
#
# [100318] shu-zu-zhong-de-ni-xu-dui-lcof
#
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        q = []
        res = 0
        for num in nums:
            # 都变成负数插入
            i = bisect.bisect_left(q,-num)
            res += i
            q.insert(i,-num)
        return res
# @lc code=end