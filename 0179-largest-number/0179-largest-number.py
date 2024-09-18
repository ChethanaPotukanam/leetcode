from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if(len(nums)==1):
            return str(nums[0])
        str_nums = list(map(str,nums))
        def compute_sort(a,b):
            if(a+b > b+a):
                return -1
            elif(a+b < b+a):
                return 1
            else:
                return 0
        str_nums.sort(key=cmp_to_key(compute_sort))
        largest_num = ''.join(str_nums)
        return 0 if largest_num[0]=='0' else largest_num