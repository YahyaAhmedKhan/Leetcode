class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        l, r = 0, n-1
        # st = set()
        st = set()
        for i in range(n-2):
            a = nums[i]
            l, r = i+1, n-1

            while l<r:
                b, c = nums[l], nums[r]
                sm = a+b+c
                if sm<=0:
                    if sm==0:
                        st.add((a, b, c))
                    l+=1
                else:
                    r-=1
            
        return list(map(list, st))




        