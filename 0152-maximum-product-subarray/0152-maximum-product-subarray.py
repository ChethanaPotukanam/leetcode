class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxp=int(float('-inf'))
        # n=len(nums)    
        # for i in range(n):
        #     p=nums[i]
        #     for j in range(i+1,n):
        #         p*=nums[j]
        #         maxp=max(maxp,p)
        # return maxp
        maxp=float('-inf')
        n=len(nums)
        pre,suf=1,1
        for i in range(n):
            if(pre==0):pre=1
            if(suf==0):suf=1
            pre*=nums[i]
            suf*=nums[n-i-1]
            maxp=max(maxp,max(pre,suf))
        return maxp