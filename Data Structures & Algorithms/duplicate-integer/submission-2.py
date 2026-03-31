class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # Like a hashmap but keys only, no vals
        for num in nums: # Loop through each number in set
            if num in seen: # if the number is in the set
                return True # Return true
            seen.add(num) # if not, add it
        return False