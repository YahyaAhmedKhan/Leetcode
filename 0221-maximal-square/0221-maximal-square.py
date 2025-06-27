class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])

        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] else 0
        for i in range(n):
            dp[0][i] = 1 if matrix[0][i] else 0

        print(dp)

        def check(i, j):
            ans = 0
            while 0<=i-ans and 0<=j-ans and matrix[i-ans][j] and matrix[i][j-ans]:
                ans+=1
            return ans

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j]:
                    maxi = check(i, j)
                    if maxi>=dp[i-1][j-1]+1:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = maxi
        for c in dp: print(c)

        maxi = 0
        for i in dp:
            maxi = max(maxi, max(i))

        return maxi**2

        

        