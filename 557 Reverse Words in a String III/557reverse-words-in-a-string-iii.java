class Solution {
    public String reverseWords(String s) {
        String[] words = s.split(" ");
        s = "";
        for (String S : words){
            char[] c = S.toCharArray();
            for (int i=0; i<c.length/2; i++){
                char temp = c[c.length-1-i];
                c[c.length-1-i] = c[i];
                c[i] = temp;
            }
            s += String.valueOf(c);
            s += " ";
        }
        return s.substring(0,s.length()-1);
    }
}