class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        counts = {}

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

            if counts[n] > majority:
                return n