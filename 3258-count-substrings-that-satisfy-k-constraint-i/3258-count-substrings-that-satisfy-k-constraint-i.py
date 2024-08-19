class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        c=0
        n=len(s)
        for i in range(n):
            for j in range(i,n):
                ss=s[i:j+1]
                if(ss.count('0')<=k or ss.count('1')<=k):
                    c+=1
        return c 