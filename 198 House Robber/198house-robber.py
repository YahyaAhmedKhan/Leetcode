class Solution:
    def rob(self, nums: List[int]) -> int:
        arr = [ -1 for i in range (len(nums))]
        print(arr)
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums[0], nums[1])
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            arr[i] = max(nums[i] + arr[i-2], arr[i-1])

        return arr[l-1]