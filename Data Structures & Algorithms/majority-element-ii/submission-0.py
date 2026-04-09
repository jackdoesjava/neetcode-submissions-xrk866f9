class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        result = []
        threshold = len(nums) // 3

        for num in nums: # Building the freq map
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            if count > threshold:
                result.append(num) # Add num to final list

        return result


        
