class Solution:
    # def pro(nums):
    #     p=1
    #     for i in nums:
    #         p*=i
    #     return p
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=0
        p=1
        for i in nums:
            if i==0:
                zero+=1
            else:
                p*=i
        ans=[]
        if zero==1:
            for i in nums:
                if i==0:
                    ans.append(p)
                else:
                    ans.append(0)
        elif(zero==0):
            for i in nums:
                ans.append(p//i)
        elif(zero>1):
            for i in nums:
                ans.append(0)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        # answer=[]
        # for i in range(len(nums)):
        #     temp=nums[i]
        #     nums[i]=1
        #     answer.append(Solution.pro(nums))
        #     nums[i]=temp
        # return answer