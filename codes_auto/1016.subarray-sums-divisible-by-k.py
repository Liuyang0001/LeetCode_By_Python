#
# @lc app=leetcode.cn id=1016 lang=python3
#
# [1016] subarray-sums-divisible-by-k
#
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans
# @lc code=end