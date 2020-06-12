#
# @lc app=leetcode.cn id=1582 lang=python3
#
# [1582] design-browser-history
#
class BrowserHistory:

    def __init__(self, homepage: str):
        self.str = [homepage]
        self.cur = homepage

    def visit(self, url: str) -> None:
        if self.str[-1]==self.cur:
            self.str.append(url)
        else:
            while self.str[-1]!=self.cur:
                self.str.pop(-1)
            self.str.append(url)
        self.cur =url


    def back(self, steps: int) -> str:
        idx =0
        n = len(self.str)
        for i in range(n):
            if self.str[i]==self.cur:
                idx = i
                break
        end = max(idx-steps,0)
        self.cur = self.str[end]
        return self.cur
        

    def forward(self, steps: int) -> str:
        idx =0
        n = len(self.str)
        for i in range(n):
            if self.str[i]==self.cur:
                idx = i
                break
        end = min(idx+steps,n-1)
        self.cur = self.str[end]
        return self.cur


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end