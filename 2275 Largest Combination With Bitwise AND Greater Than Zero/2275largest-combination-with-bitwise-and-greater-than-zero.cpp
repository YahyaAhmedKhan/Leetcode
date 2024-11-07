class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        int n = candidates.size();

        int maxx = candidates[0];
        for (int i=0; i<n; i++) maxx = max(maxx, candidates[i]);

        int ans = INT_MIN;
        for (int mask=1; mask<=maxx; mask = mask<<1){
            cout << maxx << " " << mask << endl;
            int temp = 0;
            for (int i=0; i<n; i++){
                if ( (candidates[i] & mask) > 0 ) temp++;
            }
            ans = max(ans, temp);
        }

        return ans;
        
        
    }
};