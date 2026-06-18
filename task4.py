class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3=nums1+nums2
        nums3.sort()
        
        result=0

        if (len(nums3)%2==0):
            index=len(nums3)/2
            i1=int(index-0.5)
            i2=int(index+0.5)
            result=(nums3[i1]+nums3[i2])/2
        else:
            index=int((len(nums3)/2)+0.5)-1
            result=nums3[index]

        return result