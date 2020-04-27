#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s: return ""
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] in stack:
                continue
            while stack and ord(s[i]) < ord(stack[-1]) and \
                    s.find(stack[-1], i) != -1:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)
# @lc code=end

