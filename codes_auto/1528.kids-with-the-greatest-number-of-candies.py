#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] kids-with-the-greatest-number-of-candies
#
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        tem_max = max(candies)
        res = []
        for i in candies:
            if i +extraCandies>=tem_max:
                res.append(True)
            else:
                res.append(False)
        return res
# @lc code=end