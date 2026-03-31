class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs: # if strings are empty
            return "" # no prefix

        for i, char in enumerate(strs[0]): # targets very first str
            for word in strs: # curr string in str block
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]
                
        return strs[0] # first str is prefix for every other str