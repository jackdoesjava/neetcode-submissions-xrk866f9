class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted = []

        for num in nums:
            n = num * num
            sorted.append(n)
        sorted.sort()

        
        return sorted