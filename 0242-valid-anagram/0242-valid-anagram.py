class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hasharray = [0]*26
        n = len(s)
        for i in range(n):
            j = ord(s[i])-97
            hasharray[j]+=1
            k = ord(t[i])-97
            hasharray[k]-=1
        for i in hasharray:
            if(i!=0):
                return False
        return True