class Solution {
    public static int myAtoi(String s) {
        String ans = "0";
        for (int i = 0; i < s.length(); i++) {

            if (s.charAt(i) == '+' || s.charAt(i) == '-') {
                char sign = s.charAt(i);
                for (int j = i + 1; j < s.length(); j++) {
                    if (Character.isDigit(s.charAt(j))) {
                        ans += Character.toString(s.charAt(j));
                    } else {
                        if (sign == '-')
                            try {
                                return -1*Integer.parseInt(ans);
                            } catch (java.lang.NumberFormatException e) {
                                return Integer.MIN_VALUE;
                            }
                        if (sign == '+')
                            return answ(ans);

                    }
                }
                if (sign == '-')
                    try {
                        return -1*Integer.parseInt(ans);
                    } catch (java.lang.NumberFormatException e) {
                        return Integer.MIN_VALUE;
                    }
                if (sign == '+')
                    return answ(ans);
            }
            if (Character.isDigit(s.charAt(i))) {
                for (int j = i; j < s.length(); j++) {
                    if (Character.isDigit(s.charAt(j))) {
                        ans += Character.toString(s.charAt(j));
                    } else
                        return answ(ans);
                }
                return answ(ans);
            }

            if (!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ' && s.charAt(i) != '+' && s.charAt(i) != '-')
                return 0;

        }
        return 0;

    }

    public static int answ(String s) {
        try {
            return Integer.parseInt(s);
        } catch (java.lang.NumberFormatException e) {
            return Integer.MAX_VALUE;
        }

    }

    public static void main(String[] args) {
        System.out.println(myAtoi("   -42"));
        
    }

}
