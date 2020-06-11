#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] restore-ip-addresses
#
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        # count记录分割次数, ip记录当前的字符串, s记录剩余字符串
        def backtrack(count, ip, s):
            if count == 4:
                if s=="": # 最后面会有个点号
                    res.append(ip[:-1])
                return
            if len(s) > 0:
                backtrack(count + 1, ip + s[:1] + ".", s[1:])
            if len(s) > 1 and s[0] != "0":
                backtrack(count + 1, ip + s[:2] + ".", s[2:])
            if len(s) > 2 and s[0] != "0" and int(s[:3]) < 256:
                backtrack(count + 1, ip + s[:3] + ".", s[3:])
                

        backtrack(0, "", s)
        return res
# @lc code=end