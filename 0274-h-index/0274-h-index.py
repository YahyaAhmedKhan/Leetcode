class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        hindex = [0] *(n+1)

        for c in citations:
            hindex[min(c, n) ]+=1

        for i in range(n-1, -1, -1):
            hindex[i] += hindex[i+1]

        ans = 0
        for i in range(n+1):
            if hindex[i] >= i:
                ans = max(ans, i)

        return ans