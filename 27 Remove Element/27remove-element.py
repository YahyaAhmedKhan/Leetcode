class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        curr = 0
        for i in nums:
            if (i != val):
                nums[curr] = i
                curr += 1
        return curr
