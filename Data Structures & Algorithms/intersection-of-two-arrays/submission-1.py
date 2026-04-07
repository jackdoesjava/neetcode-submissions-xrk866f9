class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        results = set()

        for num in nums2:
            if num in seen:
                results.add(num)
        
        return list(results)
        # return list(set(nums1) & set(nums2))