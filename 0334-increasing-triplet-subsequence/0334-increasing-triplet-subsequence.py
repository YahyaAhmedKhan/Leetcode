class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = nums[0]
        min2 = float("inf")

        for i in nums:
            if i > min2:
                return True
            if i > min1:
                min2 = min(min2, i)
            if i < min1:
                min1 = i
        return False