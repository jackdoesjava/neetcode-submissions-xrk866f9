class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # put each val in hashmap
        # then i want to find k most frequent numbers
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        return sorted(seen, key=seen.get, reverse=True)[:k]