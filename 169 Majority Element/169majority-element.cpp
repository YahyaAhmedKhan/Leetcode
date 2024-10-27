class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int curr = nums[0];
        int c = 1;
        for (int i=1; i<nums.size(); i++){
            if (nums[i] == curr){
                c++;
            }
            else {
                c --;
                if (c == 0) {
                    curr = nums[i];
                c = 1;
                }
            }

        }
        return curr;
    }
};