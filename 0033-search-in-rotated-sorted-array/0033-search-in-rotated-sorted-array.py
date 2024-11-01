class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f , l = 0 , n-1
        while(f<=l):
            mid = round((f+l)/2)
            if(nums[mid]==target):
                return mid
            elif(nums[f]<=nums[mid]):
                if(target>=nums[f] and target<=nums[mid]):
                    l = mid-1
                else:
                    f = mid+1
            else:
                if(target>=nums[mid] and target<=nums[l]):
                    f = mid+1
                else:
                    l = mid-1
        return -1