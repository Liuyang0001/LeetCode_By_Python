#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#
from typing import List
from collections import defaultdict
# @lc code=start
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tw = []
        # 使用defaultdict可以省去很多判断
        self.follow_dic = defaultdict(list)

    # 发推特：（用户id，发的推特id）
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tw.append((userId,tweetId))

    # 获取最新的十条推特
    def getNewsFeed(self, userId: int) -> List[int]:
        res, count = [], 0
        recept_id = [userId]+self.follow_dic[userId]
        for user,tweet in self.tw[::-1]:
            if user in recept_id:
                res.append(tweet)
                count+=1
                if count>=10: break
        # print(res)
        return res

    # 关注用户
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_dic[followerId]+=[followeeId]

        
    # 取关用户
    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.follow_dic[followerId].remove(followeeId)
        except:
            pass  


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

