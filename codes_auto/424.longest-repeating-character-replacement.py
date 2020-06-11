#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] longest-repeating-character-replacement
#
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        tem = defaultdict(int)
        res = 0
        for right, val in enumerate(s):
            tem[val] += 1
            # 找到目前最大字符个数,看该窗口是否多余翻转k个字符
            while right - left + 1 - max(tem.values()) > k:
                tem[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res

# @lc code=end