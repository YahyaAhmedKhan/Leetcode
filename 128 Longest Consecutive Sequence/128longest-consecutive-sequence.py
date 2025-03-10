class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        print(nums)
        maxi = 0
        curr = 1
        l = len(nums)
        for i in range(1, l):
            if nums[i] == nums[i-1] + 1:
                curr += 1
            elif nums[i-1] < nums[i]:
                maxi = max(curr, maxi)
                curr = 1
        maxi = max(curr, maxi)
        
        return maxi
                
            
        return ans

        