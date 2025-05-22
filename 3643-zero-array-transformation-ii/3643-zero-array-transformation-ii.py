class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        def check(q):
            nonlocal n
            arr = [0]*n
            for i in range(q):
                l, r, val = queries[i][0], queries[i][1], queries[i][2] 
                arr[l] +=val
                if r+1<n: arr[r+1]-=val
            for i in range(n):
                if i>0:
                    arr[i] += arr[i-1]

            for i in range(n):

                if nums[i]>arr[i]:
                    return False
            return True

        if not check(len(queries)): return -1

        l, r = 0, len(queries)
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                r=mid-1
            else:
                l=mid+1

        return ans
        
        