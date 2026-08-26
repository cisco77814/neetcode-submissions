class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        for i in s:
            if i in counts_s:
                counts_s[i] += 1
            else:
                counts_s[i] = 1
        counts_t = {}
        for j in t:
            if j in counts_t:
                counts_t[j] += 1
            else:
                counts_t[j] = 1
        if counts_t == counts_s:
            return True
        else:
            return False