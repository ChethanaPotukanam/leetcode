import math
MAX_INT = 2**31 - 1
MIN_INT = -2**31
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1 # 2,147,483,647
        MIN_INT = -2 ** 31    #-2,147,483,648
        reverse = 0

        while x != 0:
            if reverse > MAX_INT / 10 or reverse < MIN_INT / 10:
                return 0
            digit = x % 10 if x > 0 else x % -10
            reverse = reverse * 10 + digit
            # x = x // 10
            # don't use above line for negative numbers use math.trun function
            x=math.trunc(x/10)
        return reverse
        
        # temp = abs(x)
        # rev = 0
        # while(temp > 0):
        #     r = temp % 10
        #     rev = rev * 10 + r
        #     if(rev>MAX_INT):
        #         return 0
        #     temp=temp//10
        # if(x<0):
        #     return -rev
        # return rev

        # If there is no limit on size
        # temp = abs(x)
        # rev = 0
        # while(temp > 0):
        #     r = temp % 10
        #     rev = rev * 10 + r
        #     temp=temp//10
        # if(x<0):
        #     return -rev
        # return rev
