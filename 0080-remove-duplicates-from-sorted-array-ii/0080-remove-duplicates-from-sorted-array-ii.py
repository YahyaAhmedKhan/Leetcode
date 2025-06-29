class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0

        currnum, count = nums[0], 0

        for val in nums:
            if val!=currnum:
                currnum = val
                count=1
                nums[curr] = val
                curr+=1
            else:
                if count<2:
                    count+=1
                    nums[curr] = val
                    curr+=1

        return curr

        