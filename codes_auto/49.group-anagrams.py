#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] group-anagrams
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())
# @lc code=end