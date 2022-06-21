class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <2) return nums.length;
        int curr = nums[0];
        int pos = 1;
        for (int i=1; i<nums.length; i++){
            if (nums[i]!=curr){
                curr = nums[i];
                nums[pos] = curr;
                pos++;
            }
        }
        return pos;
    }
}