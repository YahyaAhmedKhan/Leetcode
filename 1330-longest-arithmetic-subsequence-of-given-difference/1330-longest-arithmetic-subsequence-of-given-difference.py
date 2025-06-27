class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        k = difference

        dc = {}
        for i in range(n):
            curr = arr[i]
            if (curr-k) in dc:
                dc[curr] = dc[curr-k]+1
            dc[curr] = 1 if curr not in dc else dc[curr]

        return max(list(dc.values()))
        # dp = [1]*n

        # for i in range(1, n):
        #     for j in range(i):
        #         if arr[i]-k==arr[j]:
        #             dp[i] = max(dp[i], dp[j]+1)
        # return max(dp)