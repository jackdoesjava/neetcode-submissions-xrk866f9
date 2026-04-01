class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Could sort but that's O(nlogn)
        longest = 0 # consecutive sequence
        numberSet = set(nums) # Add arr to hashset

        for num in numberSet: # Every num in set
            if (num - 1) not in numberSet: # If e.g. 4-3 wasnt in set
                length = 1
                while (num + length) in numberSet: # not empty 5
                    length += 1
                longest = max(length, longest)
        return longest