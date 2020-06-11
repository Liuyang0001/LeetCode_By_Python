#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] contains-duplicate-ii
#
        
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        for i,num in enumerate(nums):
            if dic[num]:
                if i-dic[num][-1]<=k:
                    return True
            dic[num].append(i)
        print(dic)
        return False
# @lc code=end