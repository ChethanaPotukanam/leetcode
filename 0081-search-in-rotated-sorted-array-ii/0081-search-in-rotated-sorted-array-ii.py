class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        f , l = 0 , n-1
        while(f<=l):
            mid = (f+l)//2
            if(nums[mid]==target):
                return True
            if(nums[mid]==nums[f] and nums[mid]==nums[l]):
                f+=1
                l-=1
            elif(nums[f]<=nums[mid]):
                if(target<=nums[mid] and target>=nums[f]):
                    l = mid-1
                else:
                    f = mid+1
            else:
                if(target>=nums[mid] and target<=nums[l]):
                    f=mid+1
                else:
                    l=mid-1
        return False