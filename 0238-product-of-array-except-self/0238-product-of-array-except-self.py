class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [0] * len(nums)
        suff = [0] * len(nums)
        pre[0] = 1
        suff[-1] = 1
        n = len(nums)
        for i in range(1, n):
            pre[i] = pre[i-1]*nums[i-1]
        
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1]*nums[i+1]
        ans = [pre[i]*suff[i] for i in range(n)]
        # print(pre)
        # print(suff)
        return ans
        
        