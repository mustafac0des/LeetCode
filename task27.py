class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        occurences = nums.count(val)

        for i in range(occurences):
            nums.remove(val)

        k = len(nums)

        return k
        