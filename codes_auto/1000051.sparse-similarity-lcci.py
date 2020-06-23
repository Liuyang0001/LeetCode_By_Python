#
# @lc app=leetcode.cn id=1000051 lang=python3
#
# [1000051] sparse-similarity-lcci
#
class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        ans = []
        d = collections.defaultdict(list)
        for i, arr in enumerate(docs):
            for j in arr:
                d[j].append(i)
        c = collections.Counter((i, j) for arr in d.values() for i, j in itertools.combinations(arr, 2))
        for (i, j), t in c.items():
            r = t / (len(docs[i]) + len(docs[j]) - t)
            r and ans.append(f'{i},{j}: {r + 1e-9:.4f}')
        return ans
# @lc code=end