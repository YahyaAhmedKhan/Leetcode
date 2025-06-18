class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k):
            hrs = 0
            for pile in piles:
                hrs += int(ceil(pile/k))
            return hrs<=h

        l, r = 1, max(piles)
        mini = r
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                mini = mid
                r = mid-1
            else:
                l= mid+1

        return mini
                
        