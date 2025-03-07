import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def func(mid, h, piles):
            cnt = 0
            for i in piles:
                cnt+=math.ceil(i/mid)
                if(cnt>h):
                    return False
            if(cnt<=h):
                return True
        low, high = 1, max(piles)
        final_ans = high
        while(low<=high):
            mid=(low+high)//2
            ans = func(mid,h,piles)
            if(ans):
                high = mid-1
                final_ans = mid
            else:
                low = mid+1
        return final_ans