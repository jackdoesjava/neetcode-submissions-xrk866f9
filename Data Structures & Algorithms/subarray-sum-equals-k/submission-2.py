class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        book = {0: 1} # Sum of 0 has been seen once
        total_sum = counter = 0 # Keeps track of running sum and stores how 
        # many subarrays we find that sum to k

        for num in nums: # Loop through each number in arr
            total_sum += num # Add curr num to running total
            target = total_sum - k
            if target in book:
                counter += book[target]
            
            book[total_sum] = book.get(total_sum, 0) + 1
        
        return counter
