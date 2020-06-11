#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] two-sum
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int) # 哈希字典
        for i,num in enumerate(nums):
            if num in dic: return [dic[num],i]
            dic[target-num]=i
# @lc code=end