#
# @lc app=leetcode.cn id=1000040 lang=python3
#
# [1000040] group-anagrams-lcci
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            tem = "".join(sorted(word))
            if dic.get(tem,[]):
                dic[tem].append(word)
            else:
                dic[tem] = [word]
        return list(dic.values())
# @lc code=end