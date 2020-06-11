#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] design-twitter
#
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tw = []
        # self.users = []
        self.follow_dic = defaultdict(list)

    # 发推特
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tw.append((userId,tweetId))

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

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_dic[followerId]+=[followeeId]

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
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