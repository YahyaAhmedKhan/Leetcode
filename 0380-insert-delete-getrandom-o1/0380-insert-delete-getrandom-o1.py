class RandomizedSet:

    def __init__(self):
        self.dc = {}
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.dc:
            return False
        else:
            self.arr.append(val)
            self.dc[val] = len(self.arr)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.dc:
            return False
        else:
            i = self.dc[val]
            self.arr[i]= self.arr[-1]
            self.arr.pop()
            if i<len(self.arr):
                self.dc[self.arr[i]] = i
                
            del self.dc[val]
            return True
        
    def getRandom(self) -> int:
        n = len(self.arr)
        return self.arr[randint(0, n-1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()