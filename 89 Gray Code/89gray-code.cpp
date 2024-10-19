class Solution {
public:
    vector<int> grayCode(int n) {        
        if (n==1) return vector<int> {0,1};
        else {
            vector<int> prev = grayCode(n-1);
            for (int i=prev.size()-1; i>-1; i--){
                prev.push_back(((1<<n-1) | prev[i]));
            }
            return prev;
        }
    }
};