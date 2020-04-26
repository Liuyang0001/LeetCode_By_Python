#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#
import collections
# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a, b = 0, 0
        n = len(secret)
        secret1 = []
        guess1 = []
        for i in range(n):
            if secret[i] == guess[i]:
                a += 1
            else:
                secret1.append(secret[i])
                guess1.append(guess[i])
        for item in guess1:
            if item in secret1:
                b += 1
                secret1.remove(item)
        return '{}A{}B'.format(a,b)        
# @lc code=end

