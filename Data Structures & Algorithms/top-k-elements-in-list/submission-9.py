class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        counts_arr = [[k, counts[k]] for k in counts.keys()]

        return [i[0] for i in sorted(counts_arr, key=lambda x: x[1], reverse=True)[:k]]
