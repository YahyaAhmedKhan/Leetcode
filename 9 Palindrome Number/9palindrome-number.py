class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        n = temp % 10
        temp //= 10
        while temp > 0:
            n *= 10
            n += temp % 10
            temp //= 10
        return (n == x)