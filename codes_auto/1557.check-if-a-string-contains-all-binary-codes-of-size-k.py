#
# @lc app=leetcode.cn id=1557 lang=python3
#
# [1557] check-if-a-string-contains-all-binary-codes-of-size-k
#
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        for i in range(2**k):
            tem = bin(i)[2:]
            tem = "0"*(k-len(tem))+tem
            print(tem)
            if tem not in s:
                return False
        return True
# @lc code=end