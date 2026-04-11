class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums) # Total amount of elements in arr
        for i in range(n): # Visit each index in arr from 0 to n - 1
        # Putting nums in correct position (cyclic sort of idea)
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]: 
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
                
        for i in range(n): # Find the missing number
            if nums[i] != i + 1:
                return i + 1

        return n + 1