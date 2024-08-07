class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict)
        c=0
        i=1
        for key in sorted_dict.keys():
            if(i<=8):
                c+=sorted_dict[key]
            elif(i<=16):
                c+=(2*sorted_dict[key])
            elif(i<=24):
                c+=(3*sorted_dict[key])
            else:
                c+=(4*sorted_dict[key])
            i+=1
        return c        