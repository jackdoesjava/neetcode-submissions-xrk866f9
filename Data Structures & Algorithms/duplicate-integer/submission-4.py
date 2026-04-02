class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create set
        # add numbers to set 
        # if number already in set return true
        # if all numbers can go in set, return true
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

            
