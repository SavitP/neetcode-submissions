class Twitter:

    def __init__(self):
        self.con = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.con:
            self.con[userId] = {userId}
        stack = []
        toReturn = []
        while len(toReturn) < 10 and len(self.tweets) > 0:
            ui, ti = self.tweets.pop()
            if ui in self.con[userId]:
                toReturn.append(ti)
            stack.append((ui, ti))
        while len(stack) > 0:
            self.tweets.append(stack.pop())
        return toReturn
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.con:
            self.con[followerId] = {followerId}
        self.con[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.con[followerId].discard(followeeId)
