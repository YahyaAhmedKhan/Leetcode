class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = speed.size();
        vector<float> time(n);
        vector<pair<int, float>> d(n);


        for(int i=0; i<n; i++){
            time[i] = (((target-position[i]) * 1.0 )/ speed[i] );
            d[i] = {position[i], time[i]};
        }

        sort(d.begin(), d.end());

        for(int i=0; i<n; i++) cout << "{" << d[i].first <<","<<d[i].second<<"}" <<", ";

        int ans = n;
        for (int i=n-1; i>=1; i--){
            if (d[i].second >= d[i-1].second) {
                ans--;
                d[i-1].second = d[i].second;
            }
        }
        return ans;
    }
};