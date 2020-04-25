#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
from typing import List
# from collections import defaultdict
# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket = dict()
        if t < 0: return False
        for i in range(len(nums)):
            nth = nums[i] // (t + 1)
            if nth in bucket:
                return True
            if nth - 1 in bucket and abs(nums[i] - bucket[nth - 1]) <= t:
                return True
            if nth + 1 in bucket and abs(nums[i] - bucket[nth + 1]) <= t:
                return True
            bucket[nth] = nums[i]
            if i >= k: bucket.pop(nums[i - k] // (t + 1))
        return False
# @lc code=end
# 我们换种思路。 由于本题对索引有要求，
# 因此直接排序破坏了原来的索引的做法是不行的。 我们考虑使用桶排序。

# 我们将数据分到 M 个桶 中。
# 每个数字nums[i] 都被我们分配到一个桶中
# 分配的依据就是 nums[i] // (t + 1)
# 这样相邻桶内的数字最多相差2 * (t + 1)

# 不相邻的桶一定不满足相差小于等于t
# 同一个桶内的数字最多相差t
# 因此如果命中同一个桶内，那么直接返回True

# 如果命中相邻桶，我们再判断一下是否满足 相差 <= t
# 否则返回False
# 需要注意的是，由于题目有索引相差k的要求，因此要维护一个大小为k的窗口，定期清除桶中过期的数字。

