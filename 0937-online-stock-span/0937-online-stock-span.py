class StockSpanner:

    def __init__(self):
        self.st = []
        

    def next(self, price: int) -> int:
        st = self.st
        span = 1
        while st and st[-1][0]<=price:
            span += st.pop()[1]
        st.append((price, span))
        return span
            

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)