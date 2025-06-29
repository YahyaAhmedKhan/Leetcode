class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp=[None]*n

        def helper(i):
            print(i)
            if i>=len(days):
                return 0

            if dp[i] is not None:
                return dp[i]

            n7, n30= i, i
            while n7<n and days[n7]<days[i]+7:
                n7+=1
            while n30<n and days[n30]<days[i]+30:
                n30+=1

            # print(i, n7 , n30)

            dp[i] = min(costs[0] + helper(i+1), costs[1]+helper(n7), costs[2]+helper(n30))
            return dp[i]

        ans = helper(0)
        return ans

        