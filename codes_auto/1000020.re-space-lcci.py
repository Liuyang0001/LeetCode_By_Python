#
# @lc app=leetcode.cn id=1000020 lang=python3
#
# [1000020] re-space-lcci
#
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = set(dictionary)
        lens = list({len(w) for w in dictionary})
        lens.sort(reverse = True)
        N, res, i = len(sentence), 0, 0

        @functools.lru_cache(None)
        def helper(i) :
            if i >= N : return 0
            tails = []
            tails = [helper(i+l) for l in lens if i+l <= N and sentence[i:i+l] in dictionary]
            tails += [1+helper(i+1)]
            return (min(tails) if tails else 0)

        return helper(0)
# @lc code=end