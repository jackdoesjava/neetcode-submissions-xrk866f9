class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = defaultdict(list)

        for word in strs:
            count = []
            for _ in range(26):
                count.append(0)
            for c in word:
                count[ord(c)-ord('a')] += 1
            buckets[tuple(count)].append(word)
        return list(buckets.values())