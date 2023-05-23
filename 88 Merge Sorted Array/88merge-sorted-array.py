class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        i = m+n-1

        # while p2 > -1 or p1 > -1:
        #     print(f"p1:{p1} p2:{p2} i:{i}  nums2: {nums2[p2]} nums1: {nums1[p1]}") 

        #     if p1 < 0 or nums2[p2] >= nums1[p1]:
        #         nums1[i] = nums2[p2]
        #         i -= 1
        #         p2-= 1
        #     elif p2 < 0 or nums2[p2] < nums1[p1]:
        #         nums1[i] = nums1[p1]
        #         i -= 1
        #         p1 -= 1

        while p2 >= 0:
            if p1 < 0 or nums2[p2] >= nums1[p1]:
                nums1[i] = nums2[p2]
                p2 -= 1
                i -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1
                i -= 1
