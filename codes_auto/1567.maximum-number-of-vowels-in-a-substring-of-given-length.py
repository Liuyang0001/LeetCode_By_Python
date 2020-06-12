#
# @lc app=leetcode.cn id=1567 lang=python3
#
# [1567] maximum-number-of-vowels-in-a-substring-of-given-length
#
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = []
        cnt = 0
        res = 0
        for i,e in enumerate(s):
            window.append(e)
            if i>=k:
                tem = window.pop(0)
                # print(tem)
                if tem in "aeiou": 
                    cnt -=1
            if e in "aeiou": cnt +=1
            res = max(res,cnt)
        return res
                
                
# @lc code=end