class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l<r:
                temp = nums[l]
                nums[l] =nums[r]
                nums[r] = temp
                l+=1
                r-=1

        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        






        