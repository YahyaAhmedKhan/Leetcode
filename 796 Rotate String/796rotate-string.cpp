using namespace std;
class Solution {
public:
    bool rotateString(string s, string goal) {
        int n = s.size();
        string ss(n*2, '\0');
        for (int i=0; i<2*n; i++){
            ss[i] = s[i%n];
        }
            cout << ss;
         for (int i=0; i<n; i++){
            if (ss.substr(i, n) == goal) return true;
        }
        return false;

        return 0;

    }
};