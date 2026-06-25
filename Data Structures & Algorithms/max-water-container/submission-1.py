class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_space = 0
        while i < j:
            space = (j - i) * min(heights[i], heights[j])
            max_space = max(max_space, space)
            if heights[i] < heights[j]:
                i += 1
            else: j -= 1
        return max_space