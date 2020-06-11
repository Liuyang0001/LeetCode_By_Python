#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] gas-station
#
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        self.start = -1
        n = len(gas)
        start_enable = [i for i in range(n) if cost[i]<=gas[i]]
        # print(start_enable)
        for start in start_enable:
            if self.start != -1: break
            rest = 0
            for i in range(n):
                if rest>=0: # 可以到达下一站
                    rest += (gas[(i+start)%n]-cost[(i+start)%n])
                else: continue # 不能到达下一站
            if rest>=0: 
                self.start = start
                break
        return self.start
# @lc code=end