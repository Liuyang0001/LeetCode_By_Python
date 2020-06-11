#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] divide-two-integers
#
class Solution:
    def divide(self, dividend, divisor):
        sig = not ((dividend>=0) ^ (divisor > 0))       # 判断二者相除是正or负（同或操作）
        dividend, divisor = abs(dividend), abs(divisor) # 将被除数和除数都变成正数
        res = 0                                         # 用来表示减去了多少个除数，也就是商为多少
        while divisor<=dividend:
            temp_divisor,count = divisor,1
            while temp_divisor<=dividend:
                dividend-=temp_divisor
                res +=count
                count<<=1
                temp_divisor<<=1
        res = res if sig else -res
        return min(max(res,-2147483648),2147483647)


# @lc code=end