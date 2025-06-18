class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)//3
        arrs = []

        for i in range(0, 3*n, 3):
            arrs.append([nums[i], nums[i+1], nums[i+2]])

        for arr in arrs:
            if arr[-1]-arr[0]>k: return []

        return arrs
