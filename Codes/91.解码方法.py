#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1,n):
            if s[i] == "0":
                if s[i - 1] == "1" or s[i - 1] == "2":
                    dp[i + 1] = dp[i - 1]
                else:
                    return 0
            else:
                if s[i - 1] == "1" or (s[i - 1] == "2" and "1" <= s[i] <= "6"):
                    dp[i + 1] = dp[i] + dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
        return dp[n]
# @lc code=end

# 所以，算法设计如下：

# 特判，若s为空或者s[0]=="0"，返回0

# 初始化dp=[0,...,0]，长度为n+1，dp[0]=1,dp[1]=1。dp[1]=1表示第一位的解码方法，
# dp[0]的作用，在于两位时，如："12"，dp[2]=dp[1]+dp[0]。

# 遍历s，遍历区间[1,n)：

#     若s[i]=="0"：
#         若s[i-1]=="1" or s[i-1]=="2"：
#         此时，到当前位置的解码方法dp[i+1]和上上一位的相同，
#         因为上一位和本位置结合在了一起。dp[i+1]=dp[i-1]
#         否则，返回0，表示无法解码
#     否则：
#         判断何时既可以自身解码也可以和前一位结合：
#         若上一位s[i-1]=="1"，则当前位既可以单独解码也可以和上一位结合。
#         或者上一位s[i]=="2"，则此时，若1"<=s[i]<="6"，也是可以的。
#         综上，s[i-1]=="1" or (s[i-1]=="2" and "1"<=s[i]<="6")。
#         此时，dp[i+1]=dp[i]+dp[i-1]，等于上一位和上上位的解码方法之和。
#         否则，dp[i+1]=dp[i]

# 返回dp[n]
