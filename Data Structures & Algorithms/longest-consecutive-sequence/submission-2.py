class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:  # input: list of ints → output: int
        longest = 0                         # store the longest streak found so far
        numberSet = set(nums)               # convert list → set (fast lookup, removes duplicates)

        for num in numberSet:               # go through each unique number
            # only start counting if this is the BEGINNING of a sequence
            if (num - 1) not in numberSet:  # e.g. if 3 is NOT there, then 4 could be a start
                length = 1                  # start counting from this number

                # keep going forward: num, num+1, num+2, ...
                while (num + length) in numberSet:  # check if next number exists
                    length += 1             # extend the sequence

                longest = max(longest, length)  # update best answer if this streak is longer

        return longest                      # return longest sequence length