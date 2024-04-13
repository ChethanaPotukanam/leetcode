class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str2 = ""
        n = len(word1)
        n2 = len(word2)
        i = 0
        j = 0
        while i < n or j < n2:
            if i < n:
                str2 = str2 + word1[i]
                i = i + 1
            if j < n2:
                str2 = str2 + word2[j]
                j = j + 1
        return str2
