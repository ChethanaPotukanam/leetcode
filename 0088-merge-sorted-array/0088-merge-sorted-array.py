class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # brute force
        # nums1[m:m+n]=nums2
        # nums1.sort()

        i=m-1
        j=n-1
        k=m+n-1
        while(i>=0 or j>=0):
            if(i>=0 and j>=0):
                if(nums1[i]>=nums2[j]):
                    nums1[k]=nums1[i]
                    i-=1
                else:
                    nums1[k]=nums2[j]
                    j-=1
            elif(i>=0):
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        

            
            