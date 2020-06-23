#
# @lc app=leetcode.cn id=100195 lang=python3
#
# [100195] stack-of-plates-lcci
#
class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.stack = [[]]

    def push(self, val: int) -> None:
        if self.cap <= 0:
            # 如果初始容量小于0 直接return
            return
        if len(self.stack)==0 or len(self.stack[-1]) == self.cap:
            # 当栈满了，或没有栈了，则新建一个栈
            self.stack.append([])
        self.stack[-1].append(val)

    def pop(self) -> int:
        if not self.stack or not self.stack[-1]:
            return -1
        res = self.stack[-1].pop(-1)
        if len(self.stack[-1]) == 0:
            # 如果pop后栈为空，则删除该栈
            self.stack.pop(-1)
        return res

    def popAt(self, index: int) -> int:
        if index >= len(self.stack) or not self.stack[index]:
            return -1
        res = self.stack[index].pop(-1)
        if len(self.stack[index]) == 0:
            self.stack.pop(index)
        return res



# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
# @lc code=end