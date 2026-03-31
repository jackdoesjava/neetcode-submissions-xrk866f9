class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            # If char in t is not in the count or if a letter in the arr was alr 0
            if char not in count or count[char] == 0: 
                return False
            count[char] -= 1 # Decrement
        return True