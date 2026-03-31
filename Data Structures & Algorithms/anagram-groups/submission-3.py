class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # Dict of buckets
        for string in strs:
            count = [0] * 26 # 26 empty (0) bucket slots

            for char in string: # Look at every char in word
                count[ord(char) - ord('a')] += 1
                # ord(char) gives ASCII num of a char
                # we subtract 'a' so we reset count to 0
                # Since we found the letter we then add 1 to that specific slot
            ans[tuple(count)].append(string)
        
        return list(ans.values())
