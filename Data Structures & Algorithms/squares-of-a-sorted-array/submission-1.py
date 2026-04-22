class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Need to optimise with two pointers 
        # O(nlogn) to O(n)
        sorted = []

        for num in nums:
            n = num * num
            sorted.append(n)
        sorted.sort()

        
        return sorted