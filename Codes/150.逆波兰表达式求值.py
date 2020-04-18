#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import List
# @lc code=start
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        s = []
        for x in tokens:
            if x not in ops:
                s.append(x)
            else:
                a = s.pop()
                b = s.pop()
                # 这里使用 truediv 处理类似 6 / -3 的情况
                s.append(int(ops[x](int(b), int(a))))
        return int(s[0])
# @lc code=end

