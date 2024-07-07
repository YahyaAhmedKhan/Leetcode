class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        maxx = 2**31-1
        neg = x < 0
        if neg:
            x = -1 * x

        ret = x % 10
        x //= 10

        while x != 0:
            ret = ret*10 + x%10
            if (ret > maxx):
                return 0
            x //= 10
        if neg:
            return -1 * ret
        return ret
        


        