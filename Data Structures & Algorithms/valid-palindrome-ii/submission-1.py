class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                option1 = s[left+1 : right+1] # everything from left + 1 to right (keeps)
                option2 = s[left : right] # everything from left to right - 1 (keeps)
                return option1 == option1[::-1] or option2 == option2[::-1] # Does str look same when 
                # read backwards
        
        return True
            