#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] longest-palindromic-substring
#
class Solution:
    # 马拉车算法
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        # 将一个可能是偶数长/奇数长的字符串，首位以及每个字符间添加#
        test = '#'+'#'.join(s)+'#'
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 0
        for i in range(len(test)):
            left = i - 1
            right = i + 1
            step = 0
            
            while left >= 0 and right < len(test) and test[left] == test[right]:
                left -= 1
                right += 1
                step += 1
            
            if step > max_len:
                max_len = step
                start = (i - max_len) // 2
        return s[start: start + max_len]


# @lc code=end