class Solution {
    public int searchInsert(int[] nums, int target) {
        int l=0; int r=nums.length-1;
        int mid = (l+r)/2;

        while(l<r){
            mid = (l+r)/2;
            if (nums[mid]==target) return mid;
            else {
                if (target > nums[mid]) l = mid+1;
                else r = mid-1;
            }
            
        }
        if (target > nums[l])return l+1;
        else return l;
    }
}