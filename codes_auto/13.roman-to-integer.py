#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] roman-to-integer
#
class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            # 右侧的value大于当前value,减去当前值
            if (i < len(s)-1) and (hash_map[s[i]] < hash_map[s[i+1]]):
                res -= hash_map[s[i]]
            # 否则，则加上当前值
            else:
                res += hash_map[s[i]]
        return res
# @lc code=end