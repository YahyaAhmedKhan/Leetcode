from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.index = {}
        self.heaps = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        self.index[index] = number
        heappush(self.heaps[number], index)
        

    def find(self, number: int) -> int:
        if number not in self.heaps: return -1

        hp = self.heaps[number]
        while self.heaps[number]:
            if self.index[hp[0]] == number:
                return hp[0]
            heappop(hp)
        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)