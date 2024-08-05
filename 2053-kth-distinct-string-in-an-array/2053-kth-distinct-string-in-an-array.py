class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # c=0
        # for i in arr:
        #     if(arr.count(i)==1):
        #         c+=1
        #         if(c==k):
        #             return i
        # return ""        
        carr={}
        for i in arr:
            if i in carr.keys():
                carr[i]+=1
            else:
                carr[i]=1
        for i in carr:
            if(carr[i]==1):
                k-=1
            if(k==0):
                return i
        return ""
