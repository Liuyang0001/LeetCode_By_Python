#
# @lc app=leetcode.cn id=100170 lang=python3
#
# [100170] implement-queue-using-stacks-lcci
#
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.que.insert(0,x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.que.pop() if self.que else None

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.que[-1] if self.que else None

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self.que else True



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end