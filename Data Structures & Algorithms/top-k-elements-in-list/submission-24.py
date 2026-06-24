class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        counts_arr = list(counts.items())

        foo = [None] * len(nums)

        for n, count in counts_arr:
            if foo[count-1] is None:
                foo[count-1] = [n]
            else:
                foo[count-1].append(n)
        
        print(foo)

        res = []

        for n in foo[::-1]:
            if n is not None:
                res += n
            
            if len(res) == k:
                return res