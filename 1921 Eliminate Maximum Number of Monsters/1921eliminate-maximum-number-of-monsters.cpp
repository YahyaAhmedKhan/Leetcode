class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int n = dist.size();
        vector<float> time (n, 0.0);
        for (int i = 0; i<n; i++) time[i] = (dist[i]*(1.0) / speed[i]);

        sort(time.begin(), time.end());
        int kills = 0;
        for (int i=0; i<n; i++){
            if (time[i]> i) kills++;
            else break;
        }
        return kills;
    }
};