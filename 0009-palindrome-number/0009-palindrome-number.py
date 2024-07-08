class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 :
            return False
        temp=x
        rev = 0
        # It's better to use x!=0 if we are dealing with negative values
        while(x>0):
            r=x%10
            rev=rev*10+r
            x=x//10
        if(rev==temp):
            return True
        return False