class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(set(nums))
        nn = len(nums)
        l, r = 0, 0
        st = set()
        dc={}
        ans=0
        while l<nn:
            while(len(st)<n and r<nn):
                st.add(nums[r])
                dc[nums[r]] = r
                r+=1
            if len(st)==n:   
                ans+= nn-r+1
            else: break
            print(l, r)
            if dc[nums[l]] == l:
                st.remove(nums[l])
            l+=1
        return ans