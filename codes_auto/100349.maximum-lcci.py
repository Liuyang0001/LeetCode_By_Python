#
# @lc app=leetcode.cn id=100349 lang=python3
#
# [100349] maximum-lcci
#
class Solution:
    def maximum(self, a: int, b: int) -> int:
        # return [a,b][b>a]
        k = bin((a - b) & ((1 << 63) - 1))
        idx = ("0" * (64 - len(k)) + k)[2]
        return [a, b][int(idx)]
# 思路:
# 因为python的负数存储不一样,为 -0b原码.
# 所以要转为补码,然后查看符号位.
# 负数 & 0xffffffff = 原负数的补码表示.(只是样纸一样,并不是真正的原码)
# (正数)用0补齐到32位, 然后看符号位, 直接把符号位转为索引了:  [a, b][int(符号位)]
# 写完才发现,这题要64位....大数~那也一样的,就是 & 2**63-1, 即 (1 << 63) - 1 . 
# @lc code=end