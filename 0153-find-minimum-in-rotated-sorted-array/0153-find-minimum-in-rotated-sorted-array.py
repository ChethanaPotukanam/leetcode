import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        f , l = 0 , n-1
        mini = sys.maxsize
        while(f<=l):
            mid = (f+l)//2
            if(nums[f]<=nums[mid]):
                mini = min(nums[f] , mini)
                f = mid+1
            else:
                mini = min(nums[mid] , mini)
                l = mid-1
        return mini