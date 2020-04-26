import bisect
citations = [5, 4, 4, 3, 1]
n = len(citations)
ind = bisect.bisect_left(citations,4)
print(ind)
