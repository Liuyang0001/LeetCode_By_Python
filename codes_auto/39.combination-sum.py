#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] combination-sum
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        begin,end = 0,len(candidates)
        if end == 0: return []
        res,path = [],[]
        candidates.sort()
        self.helper(candidates, begin, end, target, path, res)
        return res

    def helper(self, candidates: List[int], begin: int, end: int, delta: int, path: List[int], res: List[int]):
        if delta == 0:
            res.append(path[:])
        for index in range(begin, end):
            delta_new = delta-candidates[index]
            if delta_new < 0:
                break
            path.append(candidates[index])
            self.helper(candidates, index, end, delta_new, path, res)
            path.pop()
# @lc code=end