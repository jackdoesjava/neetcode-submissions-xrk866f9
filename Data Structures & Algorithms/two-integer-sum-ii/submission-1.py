class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Init two pointers
        left = 0
        right = len(numbers) - 1

        while left < right: # keep moving until pointers meet
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1] # remember returning seats not the sum
            
            elif curr_sum < target:
                left += 1

            else:
                right -= 1