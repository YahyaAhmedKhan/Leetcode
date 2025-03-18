class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        arr = [0]*len(nums)

        for i in queries:
            arr[i[0]]+=1
            if i[1]<len(nums)-1:
                arr[i[1]+1]-=1

        sm = 0
        print(len(nums))
        for i in range(len(arr)):
            sm += arr[i]
            arr[i] = sm
        
        for i in range(len(nums)):
            if nums[i] > arr[i]:
                return False
            
        return True
        