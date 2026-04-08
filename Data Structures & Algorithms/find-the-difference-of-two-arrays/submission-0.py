class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        map2 = set(nums2)
        res0 = set()
        for num in nums1:
            if num not in map2:
                res0.add(num)

        map1 = set(nums1)
        res1 = set()
        for num in nums2:
            if num not in map1:
                res1.add(num)

        return [list(res0), list(res1)]