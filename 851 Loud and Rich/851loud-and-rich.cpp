#include <bits/stdc++.h>
class Solution {
public:
        vector<pair<int, int>> dp;
        vector<vector<int>> adj;

    

    pair<int, int> dfs(int u, vector<int>& quiet){
        if (dp[u].first != -1) return dp[u];
        else {
            if (adj[u].size() == 0) return dp[u] = {quiet[u], u };

            else {  

                pair<int, int> minn {INT_MAX, -1};

                for (int i=0; i<adj[u].size(); i++){
                    pair<int, int> d = dfs(adj[u][i], quiet);
                    if (d < minn) minn = d;
                }  
                if (quiet[u] < minn.first) minn = {quiet[u], u};

                return dp[u] = minn;
            }

        }
    }

    vector<int> loudAndRich(vector<vector<int>>& richer, vector<int>& quiet){
        int n = quiet.size();
        int r = richer.size();

        dp.resize (n);
        pair<int, int> temp = {-1, 0};

        fill(dp.begin(), dp.end(), temp );

        adj.resize (n);

        for (int i=0; i<r; i++){
            adj[richer[i][1]].push_back(richer[i][0]);
        };

        for (int i=0; i<n; i++) dfs(i, quiet);
        vector<int> ans (n);

        for (int i=0; i<n; i++) ans[i] = dp[i].second;
        return ans;

        
        
    }
};