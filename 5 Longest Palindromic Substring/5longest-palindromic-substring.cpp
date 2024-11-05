class Solution {
public:
    
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector< pair<bool , int> >> dp(n, vector<pair<bool, int>>(n));
        for (int i=0; i<n; i++ ) dp[i][i] = {1, 1}; 
        for (int i=0; i<n-1; i++ ) {
            if (s[i] == s[i+1]) dp[i][i+1] = {1, 2};
        }
        int ans = 0;
        int maxx = INT_MIN;

        for (int i=n-1; i>=0; i--){
            for(int j=i+2; j<n; j++){

                if (s[i]==s[j]) {

                    if(dp[i+1][j-1].first) {dp[i][j] = dp[i+1][j-1];
                    dp[i][j].second +=2;}
                }
                else dp[i][j] = {0, max(dp[i+1][j].second,dp[i][j-1].second )};

            }
        }
        for (int i=n-1; i>=0; i--)
            for(int j=i; j<n; j++)            
                if (dp[i][j].second > maxx) {
                    maxx = dp[i][j].second;
                    ans = i;
                }

        cout << maxx;

        return s.substr(ans, maxx);


    }
};