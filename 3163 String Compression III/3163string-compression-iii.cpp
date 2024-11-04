class Solution {
public:
    string compressedString(string word) {
        vector<string> ss{};
        int n = word.size();
        char c = word[0];
        int siz = 0;
        int cnt = 0;
        for (int i=0; i<n; i++){
            if (word[i] == c){
                cnt++;
                if (cnt == 10){
                    string a(2, '9');
                    a[1]=c;
                    ss.push_back(a);
                    c = word[i];
                    cnt = 1;
                }
            }
            else{
                string a(2, cnt+'0');
                a[1]=c;
                ss.push_back(a);
                c = word[i];
                cnt = 1;
            }
        }
        string a(2, cnt+'0');
        a[1]=c;
        ss.push_back(a);


        string ans(2*ss.size(), '\0');
        for (int i=0; i<ss.size(); i++){
            cout << ss[i] << endl;
            ans[i*2] = ss[i][0];
            ans[i*2+1] = ss[i][1];
        }

        return ans;




    }
};