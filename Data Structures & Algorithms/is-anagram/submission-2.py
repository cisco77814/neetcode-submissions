class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for i in s:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1

        count_t = {}
        for j in t:
            if j in count_t:
                count_t[j] += 1
            else:
                count_t[j] = 1
        
        if (count_s == count_t):
            return True
        
        return False