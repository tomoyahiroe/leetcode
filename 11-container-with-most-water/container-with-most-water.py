class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        ans = 0
        while i < len(height) and j > i:
            w = j - i
            h = min(height[i], height[j])
            ans = max(w*h, ans)
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return ans