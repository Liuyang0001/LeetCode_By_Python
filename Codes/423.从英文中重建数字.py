#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#
from collections import Counter
# @lc code=start
class Solution:
    def originalDigits(self, s: str) -> str:
        s = Counter(s) 
        zero = s["z"]
        two = s["w"]
        four = s["u"]
        six = s["x"]
        eight = s["g"]
        one = s["o"] - zero - two - four
        three = s["t"] - eight - two
        five = s["f"] - four
        seven = s["s"] - six
        nine = s["i"] - six - eight - five
        res = ""
        for idx, val in enumerate([zero, one, two, three, four, five, six, seven, eight, nine]):
            res += str(idx) * val
        return res
# @lc code=end
