class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(v, i) for i, v in enumerate(nums)]
        arr.sort()
        n = len(arr)
        l, r = 0, n-1
        while l<r:
            s = arr[l][0] + arr[r][0]
            if s == target: return [arr[l][1], arr[r][1]]
            if s < target:
                l+=1
            elif s> target:
                r-=1
        