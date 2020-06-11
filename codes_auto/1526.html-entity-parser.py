#
# @lc app=leetcode.cn id=1526 lang=python3
#
# [1526] html-entity-parser
#
class Solution:
    def entityParser(self, text: str) -> str:
        dic = {"&quot;":'"',
               "&apos;":"'",
               "&amp;":'&',
               "&gt;":'>',
               "&lt;":'<',
               "&frasl;":'/'}
        new = text
        for key in dic.keys():
            new = new.replace(key,dic[key])
            # print(new)
        # print(new)
        return new
# @lc code=end