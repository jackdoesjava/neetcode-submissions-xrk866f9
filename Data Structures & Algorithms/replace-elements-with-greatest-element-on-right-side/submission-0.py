class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1

        for i in range(len(arr) - 1, -1, -1):
            cur_val = arr[i]
            arr[i] = max_so_far

            if cur_val > max_so_far:
                max_so_far = cur_val

        return arr