class Solution {
    public void rotate(int[] nums, int k) {
        k = k%nums.length;
        
        int[] ret = new int[nums.length];
        for (int i = 0; i < nums.length; i++){
            ret[i] = nums[i];
        }

        for (int i = 0; i < nums.length; i++){
            nums[(i+k)%nums.length] = ret[i];
        }

    }
}