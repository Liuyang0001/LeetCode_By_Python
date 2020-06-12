#
# @lc app=leetcode.cn id=1561 lang=python3
#
# [1561] rearrange-words-in-a-sentence
#
class Solution:
    def arrangeWords(self, text: str) -> str:
        ls = text.split(" ")
        print(ls)
        ls.sort(key=lambda x: len(x))
        res = " ".join(ls)
        return res.capitalize()
# @lc code=end