class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        j=0
        n = len(arr)
        while(k>0):
            if(j<n and arr[j]==i):
                j+=1
            else:
                k-=1
            if(k==0):
                return i 
            i+=1