import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for i in range(len(nums)):
            prefix.append(nums[i] if i == 0 else nums[i] * prefix[-1])
        suffix = []
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(nums[i] if i == len(nums) - 1 else nums[i] * suffix[-1])
        suffix.reverse()
        
        
        output = []
        for i in range(len(nums)):
            output.append((prefix[i-1] if i > 0 else 1) * (suffix[i+1] if i < len(nums)-1 else 1))
        
        return output