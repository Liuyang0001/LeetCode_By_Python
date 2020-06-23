#
# @lc app=leetcode.cn id=100350 lang=python3
#
# [100350] operations-lcci
#
class Operations:
    def __init__(self):
        pass

    def calSign(self, a, b):
        pos = True
        if a < 0:
            pos = not pos
            a = self.minus(0, a)
        if b < 0:
            pos = not pos
            b = self.minus(0, b)
        return (a, b, pos)

    def minus(self, a: int, b: int) -> int:
        # 不用位运算 - 借助str
        if b < 0:
            b = int(str(b)[1:])
        else:
            b = int('-' + str(b))
        return a + b

    def multiply(self, a: int, b: int) -> int:
        # 不用位运算, 十进制乘法, 需要借助str
        a, b, pos = self.calSign(a, b)
        res = 0
        sb = str(b)
        zerobits = 0
        for c in sb[::-1]:
            n = int(c)
            cur = 0
            for i in range(n):
                cur += a
            cur = int(str(cur) + '0' * zerobits)
            zerobits += 1
            res += cur
        return res if pos else self.minus(0, res)

    def divide(self, a: int, b: int) -> int:
        # 十进制除法, 借助str
        a, b, pos = self.calSign(a, b)
        res = 0
        cur = 0
        for c in str(a):
            cur = self.multiply(10, cur) + int(c)
            cnt = 0
            while cur >= b:
                cur = self.minus(cur, b)
                cnt += 1
            res = self.multiply(10, res) + cnt
        return res if pos else self.minus(0, res)
    


# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)
# @lc code=end