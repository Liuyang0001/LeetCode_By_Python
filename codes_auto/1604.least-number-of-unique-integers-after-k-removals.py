#
# @lc app=leetcode.cn id=1604 lang=python3
#
# [1604] least-number-of-unique-integers-after-k-removals
#
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        a = Counter(arr)
        # print(a)
        a = sorted(a.items(),key = lambda x:x[1])
        res = len(a)
        tem = 0
        for i in a:
            tem += i[1]
            if tem <=k: res-=1
            else: break
        return res
# @lc code=end