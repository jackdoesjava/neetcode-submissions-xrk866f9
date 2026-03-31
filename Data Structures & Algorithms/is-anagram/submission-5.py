class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Just checking if both strings have same length
        # If they arent same length, we know they aren't anagrams to begin with
            return False
        countS = {} # Our buckets/dictionary to store amount of times we see a letter
        
        for char in s: # This will fill the buckets using string S
            countS[char] = countS.get(char, 0) + 1 # If 'a' is in the bucket, it gives us the
            # current number then increments by one
            # If 'a' is not there yet, we say 0 then increment by 1
            
        for char in t: # Loop through every char in string t
            if char not in countS or countS[char] == 0:
                return False
            countS[char] -= 1
            
        return True