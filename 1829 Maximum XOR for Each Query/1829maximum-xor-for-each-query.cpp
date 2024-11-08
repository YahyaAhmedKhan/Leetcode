class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int n = nums.size();
        vector<int> ans(n);

        int total = nums[0];
        int mask = INT_MAX << maximumBit;
        mask = ~mask;
        ans[n-1] = ((~total) & mask);
        for (int i=1; i<n; i++){
            total ^= nums[i];
            ans[n-1-i] = ((~total) & mask);
        }

        return ans;
    }
};