class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s.length()<2) return s.length();
        int l=0,r=1, ans = r-l;
        String t=s.substring(0,1);
        
        while(r<s.length()){
            while(t.indexOf(s.charAt(r))==-1){
                r++;
                t = s.substring(l,r);
                if (r==s.length()) break;
            }
            if(ans<r-l) ans = r-l;
            l++;
            t = s.substring(l,r);
        }
        return ans;
        
    }
}