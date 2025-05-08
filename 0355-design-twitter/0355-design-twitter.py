class User:
    def __init__(self):
        self.following = set()
        self.tweets = []

class Twitter:

    def __init__(self):
        self.users = defaultdict(User)
        self.curr_time = 0
        self.k = 10

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.curr_time += 1
        self.users[userId].tweets.append((self.curr_time, tweetId))        

    def getNewsFeed(self, userId: int) -> List[int]:
        user_following = self.users[userId].following
        users_to_check = user_following | {userId}
        max_heap = []

        for uid in users_to_check:
            for t_time, tid in reversed(self.users[uid].tweets[-10:]):
                heapq.heappush(max_heap, (t_time, tid))
                if len(max_heap) > self.k:
                    heapq.heappop(max_heap)

        max_heap.sort(reverse=True)
        return [tweetId for _, tweetId in max_heap]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)