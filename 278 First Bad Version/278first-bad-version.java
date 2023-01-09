/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if (n==1) return 1;
        int l = 1;
        int r = n;
        long mid = l + (r-l)/2;

        while (!isBadVersion(l)){
            mid = l + (r-l)/2;
            if (isBadVersion((int) mid)){
                r = (int) mid;
            }
            else l =(int) (mid+1);
        }
        return l;
    }
}