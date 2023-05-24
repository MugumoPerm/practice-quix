class Solution:
    def isPalindrome(self, s: str) -> bool:
        # variables
        s = s.lower()
        length = len(s)
        clean = []
        
        non_alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
        
        for i in range(length):
            if s[i] in non_alpha:
                clean.append(s[i].lower())
        
        leng = len(clean)
        left = 0
        right = leng -1
        
        if clean == []:
            return True
        else:
            for i in range(leng):
                if clean[left+i] != clean[right-i]:
                    return False
            return True

palindrome = Solution()

print(palindrome.isPalindrome("0P"))