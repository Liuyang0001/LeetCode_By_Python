#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] shuffle-an-array
#
class Solution:
    def __init__(self, nums: List[int]):
        # self.bak = nums
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        # self.nums = self.bak
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return random.sample(self.nums, len(self.nums))
        # self.nums = random.shuffle(self.nums)
        # return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end