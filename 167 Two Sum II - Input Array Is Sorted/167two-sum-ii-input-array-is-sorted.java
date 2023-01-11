class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = 1;
        while (i<numbers.length-1){
            for (j = i+1; j<numbers.length; j++){
                if (numbers[i]+numbers[j]>target) break;
                else if (numbers[i]+numbers[j]==target) return new int[] {i+1,j+1};
            }
            i++;
        }
    return null;
    }
}