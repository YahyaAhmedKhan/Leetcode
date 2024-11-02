class Solution {
public:
    int minPartitions(string n) {
        int a = -1;
        for (int i=0; i<n.size(); i++){
            char c = n[i];
            a = max(a, (c-'0') );
            if (a==9) return a;
        }
        return a;
    }
};