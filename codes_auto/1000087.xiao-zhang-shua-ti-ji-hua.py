#
# @lc app=leetcode.cn id=1000087 lang=python3
#
# [1000087] xiao-zhang-shua-ti-ji-hua
#
class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        """二分查找答案"""
        total, max_time = 0, 0
        for t in time:
            total += t
            if t > max_time:
                max_time = t

        def cal_count(k):
            """计算每天花k时间需要多少天"""
            count = 0
            tmp = 0
            cur_max = 0
            for t in time:
                tmp += t
                cur_max = max(cur_max, t)
                if tmp - cur_max > k:
                    count += 1
                    tmp = t
                    cur_max = t
            if tmp > 0:
                count += 1
            return count

        l, r = 0, total - max_time

        while l < r:
            mid = l + (r - l) // 2
            if cal_count(mid) > m:
                l = mid + 1
            else:
                r = mid

        return l
# @lc code=end