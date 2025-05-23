class Solution {
public:
    int minInsertions(string s) {
        int n = s.size();
        cout<<n;
        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int i=0; i<n; i++) dp[i][i] = 1;
        // if i == j; dp[i][j] = d[i+1][j-1]
        // else max(dp[i+1], dp[j-1])
        for (int i=n-1; i>=0; i--){
            for (int j=i+1; j<n; j++ ){
                if (s[i] == s[j]) dp[i][j] = dp[i+1][j-1] + 2;
                else {
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        return n-dp[0][n-1] + (n>40?1:0);
    }
};