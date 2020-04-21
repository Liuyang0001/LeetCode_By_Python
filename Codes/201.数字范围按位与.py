#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        t = 0
        while m != n:
            m >>= 1
            n >>= 1
            t += 1
        return n << t
# @lc code=end

# 考虑范围[m, n]，如果n比m二进制位数高的话，
# 在累计按位与的过程中，数字的每一个二进制位数必然都出现过0，
# 所以一旦出现位数不同的情况，结果必然为0。

# 程序中，m, n在向右移位的过程中，
# 如果m, n相等了，就说明累计按位与的左边肯定等于m, n此时的状态，
# 这时候就可以向左移回来了，相当于右边所有位数都补0，相等的部分照旧。

# 如果m, n位数不相等，肯定会移到底，两者都为0时才会相等停止循环，
# 这时候再向左移多少结果都是0。
