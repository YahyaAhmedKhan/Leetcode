class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        arr = list(map(tuple, intervals))
        arr.sort()

        l, r = arr[0]
        ans = []
        for i in range(1, len(arr)):
            a,b = arr[i]

            if a>r:
                ans.append([l, r])
                l = a
                r = b
            else:
                r = max(r, b)
        ans.append([l, r])

        return ans

        
        