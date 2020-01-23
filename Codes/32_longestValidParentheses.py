'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = 0
        stack = [-1]  # -1占位
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                stack.pop()  # 弹出对应的左括号索引
                # 空栈表示已经出现不合法的括号，
                # 把索引值压进栈中
                if not stack:
                    stack.append(i)
                else:
                    # i-stack中倒数第一个的索引值
                    # 为当前合法的长度大小
                    res = max(res, i - stack[-1])
        return res


# 动态规划
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if(not s):
            return 0
        res = 0
        n = len(s)
        dp = [0]*n
        for i in range(1, n):
            if(s[i] == ")"):
                if(s[i-1] == "("):
                    dp[i] = dp[i-2]+2
                if(s[i-1] == ")" and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == "("):
                    dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                res = max(res, dp[i])
        return res
