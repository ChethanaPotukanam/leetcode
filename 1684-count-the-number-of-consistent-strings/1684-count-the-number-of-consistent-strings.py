class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # count = 0
        # for i in words:
        #     flag = 1
        #     for j in i:
        #         if j not in allowed:
        #             flag=0
        #             break
        #     if(flag==1):count+=1
        # return count
        count = 0
        allowed_set = set(allowed)
        for i in words:
            flag=1
            for j in i:
                if j not in allowed_set:
                    flag=0
                    break
            if(flag==1):count+=1
        return count 