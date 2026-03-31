class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
        
        sorted_arr = []

        while heap:
            smallest = heapq.heappop(heap)
            sorted_arr.append(smallest)
        
        return sorted_arr