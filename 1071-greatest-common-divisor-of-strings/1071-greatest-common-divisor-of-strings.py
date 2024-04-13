class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n=len(str1)
        n2=len(str2)
        gcd=1
        i=1
        while(i<=n and i<=n2):
            if(n%i==0 and n2%i==0):
                gcd=i
            i+=1
        s=str1[:gcd]
        n3=len(s)
        r=n/n3
        r2=n2/n3
        if(str1 != s*int(r) or str2 != s*int(r2)):
            return ""
        else:
            return s