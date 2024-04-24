class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=sorted(nums1+nums2)
        i=len(nums)
        if((i)%2==0):
            return (nums[(i//2)-1] + nums[(i//2)])/2
        else:
            return (nums[i//2])