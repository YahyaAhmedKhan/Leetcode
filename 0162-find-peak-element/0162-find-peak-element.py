class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0

        def check(i):
            if i==0:
                if nums[i]>nums[i+1]:
                    return 0
                else: return 1

            elif i==len(nums)-1:
                if nums[-1]>nums[-2]:
                    return 0
                else: return -1

            else:
                if nums[i-1] < nums[i] > nums[i+1]:
                    return 0
                elif nums[i+1] > nums[i]:
                    return 1
                else: return -1

        n = len(nums)
        l, r = 0, n-1

        while l<=r:
            mid = (l+r)//2
            ans = check(mid)
            if ans == 0:
                return mid
            elif ans ==1:
                l=mid+1
            else: r=mid-1

        
