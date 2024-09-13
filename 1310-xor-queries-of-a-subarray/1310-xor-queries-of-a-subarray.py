class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # new_arr=[]
        # for i in queries:
        #     j,j2=i[0],i[1]
        #     xor=0
        #     for k in range(j,j2+1):
        #         xor^=arr[k]
        #     new_arr.append(xor)
        # return new_arr
        ans = []
        prefix=[]
        prefix.append(arr[0])
        n=len(arr)
        for i in range(1,n):
            prefix.append(prefix[i-1]^arr[i])
        for left,right in queries:
            if(left==0):
                ans.append(prefix[right])
            else:
                ans.append(prefix[right]^prefix[left-1])
        return ans