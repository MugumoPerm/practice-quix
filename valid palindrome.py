class Solution:
    def isPalindrome(self, s: str) -> bool:
        # variables
        length = len(s)
        
        
        clean = []
        non_alpha = "~!@#$%^&*(_+|" ":;][}{)) '' "
        
        for i in range(length):
            if s[i] not in non_alpha:
                clean.append(s[i])
         
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

print(palindrome.isPalindrome("@&^@!^TREE@(*!@7) EE5RT@ 6^&@*&@(*@&)"))