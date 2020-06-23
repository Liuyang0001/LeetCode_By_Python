#
# @lc app=leetcode.cn id=100173 lang=python3
#
# [100173] sort-of-stacks-lcci
#
class SortedStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack.sort(reverse=True)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1] if self.stack else -1

    def isEmpty(self) -> bool:
        return self.stack==[]



# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
# @lc code=end