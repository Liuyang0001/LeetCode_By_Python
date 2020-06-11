#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] combination-sum-ii
#
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
            # 剪枝
            if index!=begin and candidates[index-1]==candidates[index]:
                continue
            path.append(candidates[index])
            # 与上题的不同在于每个元素不能重复使用
            # 所以下一个区间为[index+1,end)
            self.helper(candidates, index+1, end, delta_new, path, res)
            path.pop()
# @lc code=end