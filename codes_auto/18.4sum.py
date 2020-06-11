#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 4sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        if len(nums)==4:
            return [nums] if sum(nums)==target else []
        nums.sort()
        if sum(nums[:4])>target or sum(nums[-4:])<target:
            return []
        res=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                low = j+1
                high = len(nums)-1
                while low < high:
                    sum_four=nums[i]+nums[j]+nums[low]+nums[high]
                    cur_list=[nums[i],nums[j],nums[low],nums[high]]
                    if sum_four==target and cur_list not in res:
                        res.append(cur_list)
                    if sum_four<=target:
                        low+=1
                    elif sum_four>target:
                        high-=1
        return res
# @lc code=end