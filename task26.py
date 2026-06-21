class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        nums.sort()
        
        i = 0

        while (i+1 != len(nums)):
            if (nums[i] == nums[i+1]):
                nums.pop(i+1)
                continue

            i += 1

        k = len(nums)

        return k