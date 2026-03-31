class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = [] # init empty list

        for num in nums: # go thorugh each num in arr
            heapq.heappush(heap, num) # puts new num at bottom of tree
            # compare it to parent, if new number is smaller then it swaps
        
        sorted_arr = [] # nums in final order

        while heap: # is not empty
            smallest = heapq.heappop(heap)
            sorted_arr.append(smallest) # appends technically tot he back of the list
        
        return sorted_arr