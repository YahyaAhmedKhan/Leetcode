class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        arr = [False for i in range(l)]
        arr[l-1] = True

        for i in range (l-2, -1, -1):
            for j in range(i+1, min(i+nums[i]+1, l)):
                if arr[j]:
                    arr[i] = True

        return arr[0]



        