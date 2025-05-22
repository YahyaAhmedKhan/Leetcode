class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = len(flowerbed)
        if n==0: return True

        def get(i):
            if i>=0 and i<f: return flowerbed[i]
            else: return 0
        
        for i in range(f):
            if get(i) == 0 and get(i-1)==0 and get(i+1)==0:
                flowerbed[i] = 1
                n-=1
                if n==0: return True
        return False
        