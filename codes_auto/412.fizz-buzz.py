#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] fizz-buzz
#
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [str(i) for i in range(n + 1)]
        # 均多一个位置0，最后剪掉
        res[:n+1:3] = ["Fizz"]*(n//3+1)
        res[:n+1:5] = ["Buzz"]*(n//5+1)
        res[:n+1:15] = ["FizzBuzz"]*(n//15+1)
        return res[1:]
# @lc code=end