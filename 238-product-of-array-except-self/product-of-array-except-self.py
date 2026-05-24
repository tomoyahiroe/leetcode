class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pps = [0]*n
        sps = [0]*n
        pp = 1
        sp = 1
        for i in range(len(nums)):
            pp = pp*nums[i]
            pps[i] = pp
            sp = sp*nums[n-i-1]
            sps[n-i-1] = sp
        ans = [0]*n
        for i in range(len(nums)):
            if i == 0:
                ans[i] = sps[1]
                continue
            if i == n-1:
                ans[i] = pps[n-2]
                continue
            ans[i] = pps[i-1] * sps[i+1]
        return ans