#
# @lc app=leetcode.cn id=100180 lang=python3
#
# [100180] insert-into-bits-lcci
#
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        if N<=M: return M
        # 构建32位字符串下标i-j为0，其他为1
        tem = "1"*(32-j-1) + "0"*(j-i+1) + "1"*i
        # 将N的i-j为置0
        # 将M左移i位
        # 两者相或即可
        return (int(tem,base=2)&N)|(M<<i)
# @lc code=end