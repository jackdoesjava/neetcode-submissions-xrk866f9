class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Creating an empty hashmap to store prev
        # Key will be num from list and val will be its position.

        for i, n in enumerate(nums): # Enumerate takes a list and returns pairs of (index, element)
        # (i,n) = unpacking
        # i gets current index, n gets current value from list
            diff = target - n # Storing the complement
            if diff in prevMap: # Checking if diff val exists as a key in prevMap
                return [prevMap[diff], i]
            prevMap[n] = i