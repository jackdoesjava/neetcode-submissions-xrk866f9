class Solution:
    def sortColors(self, nums: List[int]) -> None:
        import heapq  # Missing import
        heap = []
        for n in nums:
            heapq.heappush(heap, n)  # Pushes all colors into min-heap
        
        for i in range(len(nums)):  # Write back to original array
            nums[i] = heapq.heappop(heap)  # Pop smallest → fills nums[0:n] with 0s,1s,2s
