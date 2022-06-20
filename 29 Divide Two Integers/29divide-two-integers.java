class Solution {
    public int divide(int dividend, int divisor) {     
        if (divisor == 1){
            return dividend;
        }
        if (divisor == -1){
            if (dividend == -2147483648) return 2147483647;
            else return -dividend;
        }
        int negs = 0;
        long quotient = 0;
        long dvd = dividend;
        long dvs = divisor;
        if (dvs < 0) {
            negs++;
            dvs = -dvs;

        }
        if (dvd < 0) {
            negs++;
            dvd = -dvd;

        }
        long remainder = dvd;
        while (remainder >= dvs) {
            remainder -= dvs;
            quotient++;
        }
    if (negs == 1) quotient = -quotient;
    if (quotient > 2147483647l) return 2147483647;
    if (quotient < -2147483648l) return -2147483648;
    return (int) quotient;
    }
}