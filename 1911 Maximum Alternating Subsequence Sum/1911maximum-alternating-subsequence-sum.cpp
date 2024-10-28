class Solution {
public:
    long long helper(int i, bool pos, vector<int>& nums, vector<vector<long long>>& dp){
        if (i == nums.size()) return 0;
        if (dp[pos][i] != -1) return dp[pos][i];

        return dp[pos][i] = max(helper(i+1, pos, nums, dp), helper(i+1, !pos, nums, dp) + (pos?1:-1)*nums[i] );


    }
    
    long long maxAlternatingSum(vector<int>& nums) {

        vector<vector<long long>> dp (2, vector<long long>(nums.size()+1, -1));

        return helper(0, 1, nums, dp);


    }   
};