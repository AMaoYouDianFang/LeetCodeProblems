import collections
class RecentCounter:

    def __init__(self):
        self.que = collections.deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.que and self.que[0] < t - 3000:
            self.que.popleft()
        self.que.append(t)
        return len(self.que)

#这个解法我是看了discuss才想到的，这个方法使用一个队列，当t时间到达之后，在t-3000之前的调用全部删除，因为这些不会对后面的产生任何影响了。删除之后，求长度就好了。

#时间复杂度是O(t)，空间复杂度O(t).比上面快一点。


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)