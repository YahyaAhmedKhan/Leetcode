class RecentCounter:

    def __init__(self):
        self.dq = deque()

    def ping(self, t: int) -> int:
        dq = self.dq
        dq.append(t)
        while dq and dq[0]<t-3000:
            dq.popleft()
        return len(self.dq)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)