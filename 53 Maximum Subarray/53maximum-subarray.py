class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currmax = 0
        maxx = float("-inf")
        for i in nums:
            currmax = max(currmax + i, i)
            maxx = max(maxx, currmax)
        return maxx
