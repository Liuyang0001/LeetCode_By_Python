#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] daily-temperatures
#
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 维护一个单调递减队列 
        n = len(T)
        res = [0] * n
        que = []
        for i in range(n):
            while que and T[i] > T[que[-1]]:
                t = que.pop()
                res[t] = i - t
            que.append(i)             
        return res
# @lc code=end