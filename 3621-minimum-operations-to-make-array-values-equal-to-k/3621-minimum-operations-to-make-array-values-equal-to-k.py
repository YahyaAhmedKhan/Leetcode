class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        vals = sorted(list(set(nums)))
        if k > vals[0]: return -1
        ans = len(vals)
        ans -= 1 if vals[0] == k else 0
        return ans
            
        