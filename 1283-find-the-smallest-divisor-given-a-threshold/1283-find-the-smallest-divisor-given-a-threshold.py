import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sumi(mid, nums):
            total = 0
            for i in nums:
                total+=math.ceil(i/mid)
            return total
        low, high = 1, max(nums)
        final_ans = high
        while(low<=high):
            mid = (low+high)//2
            ans = sumi(mid, nums)
            if(ans<=threshold):
                final_ans = mid
                high = mid-1
            else:
                low = mid+1
        return final_ans