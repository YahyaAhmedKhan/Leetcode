class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dc = {}
        for i in nums:
            if i not in dc:
                dc[i] = 0
            dc[i] +=1 
        ans = 0
        print(dc)
        for val in nums:
            if val<=k:
                if dc[val]>0:
                    rem = k-val
                    if dc.get(rem, 0)>0:
                        dc[rem]-=1
                        dc[val] -=1
                        if dc[val]==-1:
                            ans-=1
                            dc[val]+=2
                        ans+=1
                        
        return ans