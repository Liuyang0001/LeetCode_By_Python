'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def divide(self, dividend, divisor):
        sig = not ((dividend >= 0) ^ (divisor > 0))       # 判断二者相除是正or负（同或操作）
        dividend, divisor = abs(dividend), abs(divisor)  # 将被除数和除数都变成正数
        res = 0                                         # 用来表示减去了多少个除数，也就是商为多少
        while divisor <= dividend:                      # 当被除数小于除数的时候终止循环
            tmp_divisor, count = divisor, 1             # 倍增除数初始化
            while tmp_divisor <= dividend:              # 当倍增后的除数大于被除数重新，变成最开始的除数
                dividend -= tmp_divisor
                res += count
                count <<= 1                             # 向左移动一位,扩大两倍
                tmp_divisor <<= 1                       # 更新除数(将除数扩大两倍)
        res_value = res if sig else -res                # 给结果加上符号
        return max(min(res_value, 2147483647), -2147483648)


if __name__ == "__main__":
    s = Solution()
    print(s.divide(20, 4))
