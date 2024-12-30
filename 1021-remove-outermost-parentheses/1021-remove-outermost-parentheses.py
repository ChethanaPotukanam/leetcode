class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        new_s = ""
        c = 0
        for i in s:
            if(i=='(' and c==0):
                c = 1
            elif(i=='(' and c!=0):
                c+=1
                new_s = new_s+i
            elif(i==')' and c>1):
                c-=1
                new_s = new_s+i
            else: # i==')' and c==1 condition
                c-=1
        return new_s