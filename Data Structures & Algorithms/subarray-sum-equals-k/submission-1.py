class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        book = {0: 1} # Sum of 0 has been seen once
        total_sum = counter = 0

        for num in nums:
            total_sum += num
            target = total_sum - k
            if target in book:
                counter += book[target]
            
            book[total_sum] = book.get(total_sum, 0) + 1
        
        return counter
