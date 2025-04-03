class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possible(nums, mid, k):
            partitions, cnt = 1, 0
            for i in nums:
                cnt+=i
                if(cnt>mid):
                    cnt=i
                    partitions+=1
            if(partitions>k):
                return False
            return True
        low, high = max(nums), sum(nums)
        final_ans = high
        while(low<=high):
            mid= (low+high)//2
            ans= possible(nums, mid, k)
            if(ans):
                final_ans= ans
                high= mid-1
            else:
                low= mid+1
        return low