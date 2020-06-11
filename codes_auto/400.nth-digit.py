#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] nth-digit
#
class Solution:
    def findNthDigit(self, n: int) -> int:
        num_list = [1, 10, 190, 2890, 38890, 488890, 5888890, \
                             68888890, 788888890, 8888888890]
        index = 0
        while n >= num_list[index]: index += 1
        start_digit_num = 10 ** (index - 1)
        from_start_n = n - num_list[index - 1]
        num_offset, num_digit_offset = divmod(from_start_n, index)
        return int(str(start_digit_num + num_offset)[num_digit_offset])
# @lc code=end