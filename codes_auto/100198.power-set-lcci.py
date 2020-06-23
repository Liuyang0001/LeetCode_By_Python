#
# @lc app=leetcode.cn id=100198 lang=python3
#
# [100198] power-set-lcci
#
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        # print(nums[3:])

        def backtrack(nums, path, res):
            res.append(path)
            if nums == []:
                return 
            for i in range(len(nums)):
                backtrack(nums[i+1:] , path + [nums[i]], res)
        
        backtrack(nums, [], res)

        return res
            

        # res = [[]]
        # for num in nums:
        #     t = res[:]
        #     for lst in t:
        #         print(lst)
        #         temp = lst + [num]
        #         res.append(temp)
        # return res

# @lc code=end