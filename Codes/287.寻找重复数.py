#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
import bisect
from typing import List
# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort() # 排序后
        left, right= 1,len(nums)
        while left < right:
            mid = (left + right) // 2
            # 小于等于mid的元素个数
            cnt = bisect.bisect_right(nums,mid)
            if cnt <= mid: left = mid + 1
            else: right = mid
        return right
 
# @lc code=end

'''二分查找小于O(n^2)
我们不要考虑数组,只需要考虑 数字都在 1 到 n 之间
示例 1:
arr = [1,3,4,2,2] 此时数字在 1 — 5 之间
        [1,2,2,3,4]
mid = (1 + 5) / 2 = 3 arr小于等于的3有4个(1,2,2,3)，1到3中肯定有重复的值
mid = (1 + 3) / 2 = 2 arr小于等于的2有3个(1,2,2)，1到2中肯定有重复的值
mid = (1 + 2) / 2 = 1 arr小于等于的1有1个(1)，2到2中肯定有重复的值
所以重复的数是 2 
'''