class Solution {
public:
    vector<int> LIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);

        for (int i=0; i<nums.size(); i++){
            for (int j=0; j<i; j++){
                if (nums[i] > nums[j]) dp[i] = max (dp[i], (dp[j] + 1));
            }
        } 
        return dp;
    }
    vector<int> LIS2(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);

        for (int i=nums.size()-1; i>=0; i--){
            for (int j=nums.size()-1; j>i; j--){
                if (nums[i] > nums[j]) dp[i] = max (dp[i], (dp[j] + 1));
            }

        } 
        return dp;

    }
    int minimumMountainRemovals(vector<int>& nums) {
        vector<int> incr = LIS(nums);
        vector<int> decr = LIS2(nums);
        vector<int> ans(nums.size());
        for (int i=0; i<nums.size(); i++) ans[i] = (incr[i]>1 && decr[i] > 1)?  incr[i] + decr[i] -1 : 0;

        int maxx = *max_element(ans.begin(), ans.end());
        return (nums.size() - maxx);
        
    }
};