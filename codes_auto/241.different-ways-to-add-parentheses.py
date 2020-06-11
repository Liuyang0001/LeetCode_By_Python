#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] different-ways-to-add-parentheses
#
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit(): return [int(input)]
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }
        res = []
        n = len(input)
        for i in range(1, n):
            if input[i] in ops:
                for left in self.diffWaysToCompute(input[:i]):
                    for right in self.diffWaysToCompute(input[i + 1:]):
                        res.append(ops[input[i]](left,right))
        return res
# @lc code=end