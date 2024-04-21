class Solution:
    # class stack:
    #     def __init__(self):
    #         self.s=''
    #     def push(self,c):
    #         self.s+=c
    #     def pop(self):
    #         self.s=self.s[:-1]
    #     def ret(self):
    #         return self.s
    def removeStars(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!='*':
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)
        # uncomment class code to execute below code
        # obj=Solution.stack()
        # for i in s:
        #     if i!='*':
        #         obj.push(i)
        #     else:
        #         obj.pop()
        # s_ans=obj.ret()
        # return s_ans