#
# @lc app=leetcode.cn id=371 lang=python3
#
# [371] 两整数之和
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 将ab取为32位整形
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        while b:
            # 只保存按位相加进位的情况
            carry = a & b
            # 取按位相加，无进位的情况
            a ^= b
            # 进位左移一位，再相加得到原结果
            b = ((carry) << 1) & 0xFFFFFFFF
            # print((a, b))
        # python最后返回的是64位，如果不对负数特殊处理，
        # 那么负数的前32位是0，最后输出的是大于32位的正数
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
# @lc code=end

