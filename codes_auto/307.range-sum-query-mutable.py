#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] range-sum-query-mutable
#
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def update(self, i: int, val: int) -> None:
        try:
            self.nums[i] = val
        except:
            pass

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end