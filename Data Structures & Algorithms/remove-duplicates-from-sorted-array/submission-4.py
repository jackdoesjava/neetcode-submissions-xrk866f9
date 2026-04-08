class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        writer = 1

        for scout in range(1, len(nums)):
            if nums[scout] != nums[scout - 1]:
                nums[writer] = nums[scout]
                writer += 1
        
        return writer