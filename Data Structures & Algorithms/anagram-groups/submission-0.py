class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        #first loop goes through every word
        for word in strs:
            count = {}

            #counts the letters of each word
            for char in word:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            
            #list cant be a dictionary key, but a tuple can
            key = tuple(sorted(count.items()))

            if key in groups:
                groups[key].append(word)
            
            else:
                groups[key] = [word] 

        return list(groups.values())
        