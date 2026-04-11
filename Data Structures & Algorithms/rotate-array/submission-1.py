class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums) # Arr len
        k = k % n # When k is larger than arr len

        def reverse(left: int, right: int) -> None: # Function for reversing
            while left < right: # until they meet
                nums[left], nums[right] = nums[right], nums[left] # Swap numbers
                left += 1 # Move left in one
                right -= 1 # Move right in one
        reverse(0, n - 1) # Reverse array
        reverse(0, k - 1) # Then reverse first k elements
        reverse(k, n - 1) # Then reverse k to end elements