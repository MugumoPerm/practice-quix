class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length = len(s)
        h = []
        for i in range(length):
            h.append(s[i])
        for i in range(length):
            if t[i] in h:
                ind = h.index(t[i])
                h.pop(ind)
        if h == []:
            return True 
        else:
            return False
                
        
anagram = Solution()

print(anagram.isAnagram("caac", "ccaa"))    