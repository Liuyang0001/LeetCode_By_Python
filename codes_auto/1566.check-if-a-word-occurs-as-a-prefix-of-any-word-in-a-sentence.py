#
# @lc app=leetcode.cn id=1566 lang=python3
#
# [1566] check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence
#
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i,e in enumerate(sentence.split(" ")):
            if e.startswith(searchWord):
                return i+1
        return -1
# @lc code=end