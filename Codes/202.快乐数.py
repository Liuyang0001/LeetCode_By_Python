#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int)->bool:     
        mem = set()
        while n != 1:
            #通过str（n）调取输入整数各个位数的值     
            n = sum([int(i)**2 for i in str(n)]) 
            if n not in mem: mem.add(n)
            else: return False
        return True
# @lc code=end