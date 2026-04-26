class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # even = []
        # odd = []
        # for num in nums:
        #     if num % 2 == 0:
        #         even.append(num)
        #     else:
        #         odd.append(num)

        # ans = even + odd
        # return ans

        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums