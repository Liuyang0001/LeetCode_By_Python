#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] super-pow
#
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = "".join(map(str,b))
        # print(b)
        return pow(a,int(b),1337)
# @lc code=end