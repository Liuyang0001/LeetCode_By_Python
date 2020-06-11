#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] permutations-ii
#
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, tem = [], []
        nums.sort()
        len_nums = len(nums)
        check = [0 for _ in range(len_nums)]
        # 调用回溯函数
        self.backtrack(nums, tem, res, check)
        return res

    # 回溯函数
    def backtrack(self, nums: List[int], tem: List[int], res: List[int], check):
        if len(tem) == len(nums):
            res.append(tem[:])
        else:
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                tem.append(nums[i])
                # 去除第i个元素的部分
                self.backtrack(nums, tem, res,check)
                check[i] = 0
        if tem == []:  # 无法pop的情况
            return
        tem.pop()


if __name__ == '__main__':
    S = Solution()
    res = S.permuteUnique([1, 1, 3])
    print(res)
# @lc code=end