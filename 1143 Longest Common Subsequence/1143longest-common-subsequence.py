class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        rows = len(text1)
        cols = len(text2)

        arr = [[-1 for _ in range(cols)] for _ in range(rows)]
        return self.lcs(text1, rows-1, text2, cols-1, arr)



    def lcs(self, s, n, t, m, arr):
        if (n==-1 or m==-1 ): return 0

        if arr[n][m] != -1:
            return arr[n][m]
        else:
            if s[n] == t[m]:
                arr[n][m] = 1 + self.lcs(s, n-1, t, m-1, arr)
                return arr[n][m]
            else:
                arr[n][m] = max(self.lcs(s, n-1, t, m, arr), self.lcs(s, n, t, m-1, arr)) 
                return arr[n][m]