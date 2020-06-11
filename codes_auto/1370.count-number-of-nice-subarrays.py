#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] count-number-of-nice-subarrays
#
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, tmp, dic = 0, 0, {0: 1}
        for num in nums:
            if num & 1:
                tmp += 1
                dic[tmp] = 1
            else:
                dic[tmp] += 1
            res += dic.get(tmp-k, 0)
        return res
# @lc code=end