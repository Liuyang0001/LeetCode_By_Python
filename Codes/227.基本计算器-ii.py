#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.strip()
        nums, signs = "0123456789", "+-*/"
        num, sign, n = "", "+", len(s)
        # 遍历整个表达式
        # 把数和"上一个"符号分别存起来
        # 上一个为加减，入栈
        # 上一个为弹栈后进行乘除运算，入栈
        # 计算栈内总和
        for i in range(n):
            ch = s[i]
            # print(stack)
            if ch in nums:
                num += ch
            if ch in signs or i== n-1:
                if sign == "+":
                    stack.append(int(num))
                elif sign == "-":
                    stack.append(-int(num))
                elif sign == "*":
                    tem = stack.pop()*int(num)
                    stack.append(tem)
                elif sign == "/":
                    # 注意这里不能用//,因为-3//2 会返回-2
                    tem = int(stack.pop()/int(num))
                    stack.append(tem)
                # 更新 数与符号
                num,sign = "",ch
        return sum(stack)
# @lc code=end