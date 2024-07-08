import math
MAX_INT = 2**31 - 1
class Solution:
    def reverse(self, x: int) -> int:
        temp = abs(x)
        rev = 0
        while(temp > 0):
            r = temp % 10
            rev = rev * 10 + r
            if(rev>MAX_INT):
                return 0
            temp=temp//10
        if(x<0):
            return -rev
        return rev

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
