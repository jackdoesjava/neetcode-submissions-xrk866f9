class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for right in range(len(nums)):
            if right >= k + 1:
                window.discard(nums[right - k - 1])
            
            if nums[right] in window:
                return True
            
            window.add(nums[right])
        
        return False
