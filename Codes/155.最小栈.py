#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_ = []
        
    def push(self, x: int) -> None:
        self.stack_.append(x)

    def pop(self) -> None:
        try:
            self.stack_.pop()
        except:
            pass

    def top(self) -> int:
        return self.stack_[-1]

    def getMin(self) -> int:
        return min(self.stack_)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

