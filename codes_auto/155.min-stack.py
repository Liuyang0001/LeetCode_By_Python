#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] min-stack
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.minst = []
        
    def push(self, x: int) -> None:
        self.st.append(x)
        bisect.insort(self.minst,x)

    def pop(self) -> None:
        try:
            x = self.st.pop()
            self.minst.remove(x)
        except:
            pass

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[0]
# @lc code=end