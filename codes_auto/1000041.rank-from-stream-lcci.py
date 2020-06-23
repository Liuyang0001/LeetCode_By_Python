#
# @lc app=leetcode.cn id=1000041 lang=python3
#
# [1000041] rank-from-stream-lcci
#
class StreamRank:

    def __init__(self):
        self.nums = []


    def track(self, x: int) -> None:
        self.nums.append(x)


    def getRankOfNumber(self, x: int) -> int:
        tem = [num for num in self.nums if num<=x]
        return len(tem)


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
# @lc code=end