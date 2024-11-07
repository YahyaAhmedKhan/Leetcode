class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();

        vector<vector<int>> dp(m, vector<int>(n));
        for (int i=0; i<m; i++) {
            dp[i][0] = !obstacleGrid[i][0]?1:0;
            if (obstacleGrid[i][0]) break;
            }
    
        for (int i=0; i<n; i++) {
            dp[0][i] = !obstacleGrid[0][i]?1:0;
            if (obstacleGrid[0][i]) break;
            }

        for (int i=1; i<m; i++){
            for (int j=1; j<n; j++){
                dp[i][j] = !obstacleGrid[i][j]? dp[i-1][j] + dp[i][j-1] : 0;
                
            }
        }
        for (int i=0; i<m; i++) 
        {
            for (int j=0; j<n; j++)
            {
                cout << dp[i][j] << " ";
                
            }
            cout << endl;

        }


        return dp[m-1][n-1];
    }
};