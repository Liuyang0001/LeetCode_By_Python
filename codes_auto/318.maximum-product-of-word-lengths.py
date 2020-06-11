#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] maximum-product-of-word-lengths
#
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        words.sort(reverse=True, key=lambda x: len(x))
        for i, word1 in enumerate(words):
            # 剪枝：后面不可能出现更大的
            if res>=len(word1)**2: break
            for word2 in words[i + 1:]:
                flag = False # 标志位：判别是否出现重复的
                for letter in word2:
                    if letter in word1:
                        flag = True
                        continue
                if flag: continue
                res = max(res, len(word1) * len(word2))
        return res
# @lc code=end