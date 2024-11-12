class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        int n = items.size();
        int m = queries.size();
        vector<int> ans(m);
        vector<pair<int, int>> itemss(n);
        for (int i=0; i<n; i++) itemss[i] = {items[i][0], items[i][1]};
        sort(itemss.begin(), itemss.end());

        for (int i=0; i<n; i++) cout << "{" << itemss[i].first << "," << itemss[i].second <<  "}, ";
        cout << endl;
        
        vector<pair<int, int>> qq(m);
        for (int i=0; i<m; i++) qq[i] = {queries[i], i};
        sort(qq.begin(), qq.end());
        for (int i=0; i<m; i++) cout << "{" << qq[i].first << "," << qq[i].second <<  "}, ";

        
        int i=0,j=0;
        int maxi = 0;
        // i goes through queries in sorted fashion
        // j goes through items, sorted by price
        while(i<m && j<n){
            ans[qq[i].second] = maxi;
            // maxi = max(maxi, itemss[j].second);

            while (itemss[j].first <= qq[i].first) { // if price <= to query[i]
                maxi = max(maxi, itemss[j].second);
                ans[qq[i].second] = maxi;
                // ans[qq[i].second] = max(itemss[j].second, ans[qq[i].second]);
                if (j==n-1){
                    while (i<m){
                        ans[qq[i++].second] = maxi;

                    }
                    return ans;
                }
                j++;

            }
            i++;
        }
        return ans;

    }
};