'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 排序
        # 设置访问数组
        check = [0 for _ in range(len(nums))]
        res, tem = [], []
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
                # 剪枝
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    continue
                check[i] = 1
                tem.append(nums[i])
                self.backtrack(nums, tem, res, check)
                check[i] = 0
        if tem == []:  # 无法pop的情况
            return
        tem.pop()


if __name__ == '__main__':
    S = Solution()
    res = S.permuteUnique([1, 1, 3])
    print(res)
