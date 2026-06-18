class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sm = sum(nums[0:k])
        ans = sm
        for i in range(len(nums)-k):
            sm = sm - nums[i] + nums[i+k]
            if ans < sm:
                ans = sm
        return ans/k