#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] reverse-words-in-a-string
#
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        res = [""]
        for i in range(len(s)):
            if s[i]==" " and s[i+1]==" ":
                continue
            elif s[i]==" ":
                res.insert(0,"")
            else:
                res[0] += s[i]
        # print(res)
        return " ".join(res) if len(res)>1 else res[0]
# @lc code=end