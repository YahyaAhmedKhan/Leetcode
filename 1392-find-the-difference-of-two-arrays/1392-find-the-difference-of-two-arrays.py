class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]

        # dc = {}
        # for i in nums1:
        #     if i not in dc:
        #         dc[i] = 0

        # for val in nums2:
        #     if val not in dc:
        #         dc[val] = 1
        #     else:
        #         dc[val] = 2

        
        
        # arr1, arr2 = [], []

        # for key in list(dc.keys()):
        #     idx = dc[key]
        #     if idx == 0: arr1.append(key)
        #     elif idx==1: arr2.append(key)

        # return [arr1, arr2]