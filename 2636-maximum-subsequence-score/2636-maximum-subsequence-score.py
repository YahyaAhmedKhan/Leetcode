class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        comb = [(nums2[i], nums1[i]) for i in range(n)]
        comb.sort()
        comb.reverse()
        for i in range(n):
            print(comb[i][1], end = " ")
        print()
        for i in range(n):
            print(comb[i][0], end = " ")

        hp = []
        s = 0
        for i in range(k):
            heappush(hp, comb[i][1])
            s+= comb[i][1]
        
        maxx = s*comb[k-1][0]
        for i in range(k, n):
            s+=comb[i][1]
            heappush(hp, comb[i][1])
            low = heappop(hp)
            s -= low
            maxx = max(maxx, s*comb[i][0])

        return maxx
            


