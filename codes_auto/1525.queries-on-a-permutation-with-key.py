#
# @lc app=leetcode.cn id=1525 lang=python3
#
# [1525] queries-on-a-permutation-with-key
#
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res=[]
        ls = [x for x in range(1,m+1)]
        for i in range(len(queries)):
            index = ls.index(queries[i])
            res.append(index)
            del ls[index]
            ls.insert(0,queries[i])
            # print(ls)
        # print(res)
        return res
# @lc code=end