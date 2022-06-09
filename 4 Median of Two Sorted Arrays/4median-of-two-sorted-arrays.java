class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums = new int[nums1.length + nums2.length];
        if(nums1.length==0){
            if(nums2.length%2==0) {
                    return (nums2[nums2.length/2]+nums2[nums2.length/2-1])/2.0;
                }
                else {
                    return (nums2[nums2.length/2]);
                }
        }
        if(nums2.length==0){
            if(nums1.length%2==0) {
                    return (nums1[nums1.length/2]+nums1[nums1.length/2-1])/2.0;
                }
                else {
                    return (nums1[nums1.length/2]);
                }
        }
        // if (nums.length==2) return (nums1[0]+nums2[0])/2.0;


        int a=0,b=0;
        for (int i=0; i<nums.length/2+1; i++){
            if (a==nums1.length){
                while(i<nums.length/2+1){
                    nums[i] = nums2[b];
                    b++;
                    i++;
                }
                if(nums.length%2==0) {
                    return (nums[nums.length/2]+nums[nums.length/2-1])/2.0;
                }
                else {
                    return (nums[nums.length/2]);
                }
            }
            if (b==nums2.length){
                while(i<nums.length/2+1){
                    nums[i] = nums1[a];
                    a++;
                    i++;
                }
                if(nums.length%2==0) {
                    
                    return (nums[nums.length/2]+nums[nums.length/2-1])/2.0;
                }
                else {
                    return (nums[nums.length/2]);
                }
            }
            if (nums1[a]<=nums2[b]){
                nums[i] = nums1[a];
                a++;
            }
            else {
                nums[i] = nums2[b];
                b++;
            }
        }
        if(nums.length%2==0) {
            return (nums[nums.length/2]+nums[nums.length/2-1])/2.0;
        }
        else {
            return (nums[nums.length/2]);
        }
    }
}