#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] longest-substring-without-repeating-characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0 # 如果字符串s为空，返回0
        n = len(s)
        left,right = 0,1
        res = 1
        while right<n:
            tem = s[left:right]
            cur = s[right]
            if cur in tem:
                # 121
                left+=(tem.index(cur)+1)
            res= max(res,right-left+1)
            right +=1

        return res

# @lc code=end