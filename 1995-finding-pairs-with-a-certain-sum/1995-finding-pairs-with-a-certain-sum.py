class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.dc1 = {}
        self.dc2 = {}
        # self.nums1 = nums1
        self.nums2 = nums2
        for i in nums1:
            self.dc1[i] = self.dc1.get(i, 0) + 1
        for j in nums2:
            self.dc2[j] = self.dc2.get(j, 0) + 1


        

    def add(self, index: int, val: int) -> None:
        a = self.nums2[index]
        if self.dc2[a]==1: del self.dc2[a]
        else: self.dc2[a]-=1

        self.nums2[index]+=val
        self.dc2[self.nums2[index]]  = self.dc2.get(self.nums2[index], 0)+1

        

    def count(self, tot: int) -> int:
        ans = 0
        for k in self.dc1.keys():
            freq = self.dc1[k]
            rem = tot-k
            ans += freq * self.dc2.get(rem, 0)
        return ans


        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)