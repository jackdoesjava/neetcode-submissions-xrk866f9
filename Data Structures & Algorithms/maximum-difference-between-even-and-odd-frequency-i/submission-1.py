class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        odd_freqs = []
        even_freqs = []

        for freq in counts.values():
            if freq % 2 == 0:
                even_freqs.append(freq)
            else:
                odd_freqs.append(freq)
            
        return max(odd_freqs) - min(even_freqs)