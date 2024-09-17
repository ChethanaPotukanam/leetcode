class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s_words=[]
        s=''
        for i in s1:
            if(i==' '):
                s_words.append(s)
                s=''
            else:
                s+=i
        s_words.append(s)
        s=''
        for i in s2:
            if(i==' '):
                s_words.append(s)
                s=''
            else:
                s+=i
        s_words.append(s)
        ans = []
        for i in s_words:
            if(s_words.count(i)==1):
                ans.append(i)
        return ans