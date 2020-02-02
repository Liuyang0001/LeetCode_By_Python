from typing import List
from collections import Counter
from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return '1'
        # 加上*，可以防止数组越界,不用考虑边界问题
        num = self.countAndSay(n - 1) + "*"
        ls = list(groupby(num))
        print(ls)
        nums_ls = list(num)
        count, res = 1, ""
        for i in range(len(nums_ls)-1):
            if nums_ls[i] == nums_ls[i+1]:
                count += 1
            elif nums_ls[i] != nums_ls[i+1]:
                res += str(count) + nums_ls[i]
                count = 1
        return res


if __name__ == "__main__":
    S = Solution()
    nums = [1, 5, 6, 6, 6, 7]
    target = 7
    res = S.countAndSay(target)
    print(res)
