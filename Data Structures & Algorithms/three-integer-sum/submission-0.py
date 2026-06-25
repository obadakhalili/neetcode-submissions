class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counts = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if i != j:
                    pairs.append([nums[i], nums[j]])

        outputs = set()
        for p in pairs:
            s = sum(p)
            c = -s

            if c in counts and (counts[c] - sum([1 for n in p if n == c])) > 0:
                outputs.add(tuple(sorted([*p, c])))
        
        return [list(o) for o in outputs]