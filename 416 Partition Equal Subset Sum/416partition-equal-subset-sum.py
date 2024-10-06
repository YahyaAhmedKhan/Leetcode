class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)  # Get the total sum of the array
        
        # If the total sum is odd, it cannot be divided into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2  # The sum each subset needs to reach
        l = len(nums)
        
        # Create a DP array to store whether a particular sum is achievable
        dp = [[False for _ in range(target + 1)] for _ in range(l + 1)]
        
        # Set the sum of 0 to True for all lengths of nums (empty subset achieves sum 0)
        for i in range(l + 1):
            dp[i][0] = True
        
        # Populate the DP array
        for i in range(1, l + 1):  # Iterate over the items
            for j in range(1, target + 1):  # Iterate over the target sums
                if nums[i - 1] <= j:  # If current item can be part of the sum
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                else:  # Otherwise, carry forward the previous state
                    dp[i][j] = dp[i - 1][j]

        # The answer will be whether the target sum is achievable using all items
        return dp[l][target]
 