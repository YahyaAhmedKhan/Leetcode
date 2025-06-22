class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        xor = 0
        for val in nums:
            xor ^= val
        return xor
        