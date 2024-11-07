class Solution {
public:
    int helper(int target, vector<int>& dp) {

        if (dp[target] != -1)
            return dp[target];

        if (target == 0)
            return dp[1] = 1;

        int ret = -1;

        for (int i = 1; i <= target; i++) {
            ret = max(ret, helper(target-i, dp)*i);
        }
        return dp[target] = ret;

    }
        int integerBreak(int n) {
            if (n==2) return 1;
            if (n==3) return 2;


            // vector<vector<int>> dp(n+1, vector<int>(n+1));
            vector<int> dp(n + 1, -1);

            return helper(n, dp);
        }
    };