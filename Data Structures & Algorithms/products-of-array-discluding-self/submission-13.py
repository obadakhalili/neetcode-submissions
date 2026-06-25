import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros_count = len([n for n in nums if n == 0])
        prod = math.prod(nums)
        non_zero_prod = math.prod([n for n in nums if n != 0])

        return [
            prod//n if n != 0 else (0 if zeros_count > 1 else non_zero_prod)
            for n in nums
        ]