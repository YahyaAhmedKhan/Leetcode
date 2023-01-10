class Solution {
    public int[] sortedSquares(int[] nums) {
        int l = 0;
        int r = nums.length-1;
        int[] retval = new int[nums.length];
        for(int i=nums.length-1; i>-1; i--){
            if (Math.abs(nums[l])>=Math.abs(nums[r])){
                retval[i] = nums[l++];
            }
            else retval[i] = nums[r--];
        }
        for (int i=0; i<nums.length; i++) retval[i] = retval[i]*retval[i];
        return retval;
    }
}