#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] dungeon-game
#
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        # 逆向dp: 从公主屋到勇士屋
        dp = [[float(inf)] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1 # 勇士需要活着「一滴血」才能从边界外走进公主屋
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                minn = min(dp[i + 1][j], dp[i][j + 1])
                # dp[i][j]表示从该房间(i, j)出发能够到达公主屋的勇士最低血量值 (「恰好」存活).
                
                # 如果房间为负数, 需要给勇士加相应的血才能保证勇士「恰好」存活; 
                # 如果房间为正数, 相当于房间「免费」补给血量, 勇士的健康值就可以降低这些 (反正降了有人给白补), 
                # 但是你要接受白嫖, 你首先得活着(即下限一滴血);
                
                # 假设你进入A房间之前「恰好」存活需要 3 滴血, 你一进入A房间发现可以白嫖 10 滴血,
                # 那么在A房间时你只需要有 1 滴血, 你就可以「右下」走到公主屋了.
                dp[i][j] = max(minn - dungeon[i][j], 1)
        return dp[0][0] # dp[0][0]: 从该房间(0, 0)出发能够到达公主屋的勇士最低血量值 (「恰好」存活).
# @lc code=end