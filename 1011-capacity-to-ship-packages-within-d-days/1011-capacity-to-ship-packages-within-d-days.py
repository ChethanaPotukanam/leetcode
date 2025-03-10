class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def cal(mid, weights, days):
            c = 0
            for i in weights:
                c+=i
                if(c==mid):
                    days-=1
                    c=0
                if(c>mid):
                    days-=1
                    c=i
            if(c>0):
                days-=1
            if(days>=0):
                return True
            else:
                return False
        low, high = max(weights), sum(weights)
        final_ans = high
        while(low<=high):
            mid = (low+high)//2
            ans = cal(mid, weights, days)
            if(ans):
                final_ans = mid
                high = mid-1
            else:
                low = mid+1
        return final_ans