from collections import defaultdict
import heapq

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
        heap = []
        user = self.users[userId]
        users_to_check = user.following | {userId}  # Include self

        for uid in users_to_check:
            for time, tid in reversed(self.users[uid].tweets[-10:]):  # only check last 10 tweets per user
                heapq.heappush(heap, (-time, tid))  # max-heap by negative time

        result = []
        while heap and len(result) < self.k:
            result.append(heapq.heappop(heap)[1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.discard(followeeId)
