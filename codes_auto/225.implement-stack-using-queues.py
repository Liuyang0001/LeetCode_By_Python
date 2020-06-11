#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] implement-stack-using-queues
#
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = []
        self.que2 = []


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.que1: return None
        while len(self.que1)>1:
            self.que2.append(self.que1.pop(0))
        res = self.que1.pop(0)
        self.que1,self.que2 = self.que2,[]
        return res


    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.que1: return None
        while self.que1:
            self.que2.append(self.que1.pop(0))
        res = self.que2[-1]
        self.que1,self.que2 = self.que2,[]
        return res


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.que1 else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end