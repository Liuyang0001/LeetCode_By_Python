#
# @lc app=leetcode.cn id=1562 lang=python3
#
# [1562] people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list
#
class Solution:
    def peopleIndexes(self, fc: List[List[str]]) -> List[int]:
        n = len(fc)
        res = []
        # fc.sort(key=lambda x: len(x))
        for i in range(n):
            flag = True
            tem = set(fc[i])
            for j in fc[:i]+fc[i+1:]:
                if tem.issubset(j):
                    flag = False
                    break
            if flag: res.append(i)
        return res
# @lc code=end