class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def func(mid,k,m,bloomday):
            cnt = 0
            total_boq = 0
            for i in bloomDay:
                if(i<=mid):
                    cnt+=1
                else:
                    total_boq+=(cnt//k)
                    cnt=0
            total_boq+=(cnt//k)
            if(total_boq<m):
                return False
            return True
        if(m*k>len(bloomDay)):
            return -1
        low, high = min(bloomDay), max(bloomDay)
        final_ans = high
        while(low<=high):
            mid=(low+high)//2
            ans = func(mid, k, m, bloomDay)
            if(ans):
                high=mid-1
                final_ans=mid
            else:
                low=mid+1
        return final_ans