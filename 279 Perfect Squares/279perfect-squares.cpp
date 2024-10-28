class Solution {
public:
    int numSquares(int n) {
        int s = 1;
        while (s*s <= n) s++;
        s--;

        vector<int> sq(s, 0);
        for (int i=0; i<s; i++) {sq[i] = (i+1)*(i+1); cout<< sq[i] << " ";}

        vector<vector<int>> dp(sq.size()+1, vector<int>(n+1, INT_MAX));
        for (int i=0;  i<sq.size()+1; i++) dp[i][0] = 0;
        for (int i=1; i<sq.size()+1; i++ ){
            for (int j=1; j<n+1; j++){
                if (j < sq[i-1]) dp[i][j] = dp[i-1][j];
                else {
                    dp[i][j] = min((1+ dp[i][j-sq[i-1]]), dp[i-1][j] );
                }
            }
        }

        return dp[sq.size()][ n];



    }
};