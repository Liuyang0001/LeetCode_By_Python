#
# @lc app=leetcode.cn id=1473 lang=python3
#
# [1473] find-the-longest-substring-containing-vowels-in-even-counts
#
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res, status = 0, 0
        # aeiou 0,1对应的情况共有32种
        pos = [0] + [-1] * 31
        # 对应的掩码
        mask = {'a':0b1,
                'e':0b10,
                'i':0b100,
                'o':0b1000,
                'u':0b10000}
        # 遍历字符串
        for i, letter in enumerate(s):
            # 不是元音，异或0不变
            status ^= mask.get(letter,0)
            # 判断状态是否出现过
            if pos[status] == -1:
                pos[status] = i + 1
            else:
                res = max(res, i + 1 - pos[status])

        return res

# @lc code=end