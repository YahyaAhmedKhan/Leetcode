class Solution {
public:
    long long minEnd(int n, int x) {
        long long ans = 0;
        ans = x;

        for (int i=1; i<n; i++ ){
            ans++;
            ans|=x;
        }
        return ans;
    }
};