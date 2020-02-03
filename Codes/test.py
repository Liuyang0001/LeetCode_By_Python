from typing import List
from collections import Counter
from itertools import groupby


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        max_size = len(candidates)
        if max_size == 0:
            return []
        res,path = [],[]
        candidates.sort()
        self.helper(candidates, 0, max_size, target, path, res)
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


if __name__ == "__main__":
    S = Solution()
    nums = [1, 5, 6, 7]
    target = 7
    res = S.combinationSum(nums,target)
    print(res)
