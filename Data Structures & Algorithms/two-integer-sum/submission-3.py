class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = i
        for j in range(len(nums)):
            c = target - nums[j]
            if c in d and d[c] != j:
                return [j, d[c]]