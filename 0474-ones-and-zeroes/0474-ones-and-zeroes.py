class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [[0,0] for _ in range(len(strs))]

        for i in range(len(strs)):
            s = strs[i]
            for c in s:
                cc = int(c)
                count[i][cc]+=1

        print(count)
        k = len(strs)
        dp = [[[None]*(n+1) for _ in range(m+1)] for _ in range(k)]


        a1, b1 = count[0][0], count[0][1]
        for i in range(m+1):
            for j in range(n+1):
                dp[0][i][j] = 1 if a1<=i and b1<=j else 0

        def helper(i, mm, nn):
            if dp[i][mm][nn] is not None:
                return dp[i][mm][nn]

            a, b = count[i][0], count[i][1]
            if a<=mm and b<=nn:
                dp[i][mm][nn] = max(helper(i-1, mm-a, nn-b)+1, helper(i-1, mm, nn))
            else:
                dp[i][mm][nn] = helper(i-1, mm, nn)

            return dp[i][mm][nn]

        return helper(len(strs)-1, m, n)



