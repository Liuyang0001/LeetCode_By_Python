#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] top-k-frequent-elements
#
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        c = Counter(nums)
        # print(c)
        lc = sorted(c.items(), key=lambda x: x[1], reverse=True)
        # print(lc)
        res = [lc[0][0]]
        # if k==1: return res
        for i in range(1, len(lc)):
            if k == 1: break
            # if lc[i][1] < lc[i - 1][1]:
            #     k-=1
            k-=1
            res.append(lc[i][0])
            
        return res


# @lc code=end