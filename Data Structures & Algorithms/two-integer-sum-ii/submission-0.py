class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while True:
            curr = nums[i] + nums[j]
            if curr > target:
                j -= 1
            elif curr < target:
                i += 1
            else:
                return [i+1, j+1]