class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        num = 0
        i , j = 0 , len(nums)-1
        while(i<=j):
            if(i!=j):
                num = num^nums[i]^nums[j]
            else:
                num = num^nums[i]
            i+=1
            j-=1
        return num