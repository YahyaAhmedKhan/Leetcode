class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = 0
        ans = 0
        for val in gain:
            s+=val
            ans = max(ans, s)

        return ans
        