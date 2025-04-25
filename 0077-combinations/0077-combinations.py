class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def helper(i, k):
            if k==0: return [[]]
            if i<k: return []
            if i == 0: return []

            choose = helper(i-1, k-1)
            for c in choose:
                c.append(i)
            notChoose = helper(i-1, k)
            for c in notChoose:
                choose.append(c)
            return choose

        ans = helper(n, k)
        return ans