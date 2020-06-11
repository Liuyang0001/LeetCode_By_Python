#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] implement-queue-using-stacks
#
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []
        self.B = []
        
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())
            return self.B.pop()
        else:
            return self.B.pop()
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())
            return self.B[-1]
        else:
            return self.B[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.B)==0 and len(self.A)==0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end