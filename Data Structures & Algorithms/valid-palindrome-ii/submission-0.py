class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                option1 = s[left+1 : right+1]
                option2 = s[left : right]
                
                # In Python, string[::-1] is the most efficient way to check a palindrome
                return option1 == option1[::-1] or option2 == option2[::-1]
        
        return True
            