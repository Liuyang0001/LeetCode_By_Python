#
# @lc app=leetcode.cn id=100320 lang=python3
#
# [100320] shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
#
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        s = 0
        # 得到两个数异或的结果
        for num in nums:
            s ^= num
        # k是二进制数低位连续的0加上一个1组成的数
        # 1说明两个只出现一次的数对应的是不同的
        # 将nums分成两个小组
        # 该位为1的，该位为0的
        # 0&a=a a&a=0
        # 最后只会剩下重复的那两个数
        k = s & (-s)
        res = [0, 0]
        for num in nums:
            if num & k:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
# @lc code=end