class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create set
        # add numbers to set 
        # if number already in set return true
        # if all numbers can go in set, return true
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
            
