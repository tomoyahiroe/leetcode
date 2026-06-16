class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        i = 0
        j = len(nums)-1
        while i < j:
            sumc = nums[i]+nums[j]
            if sumc == k:
                cnt += 1
                i += 1
                j -= 1
            elif sumc > k:
                j -= 1
            else:
                i += 1
        return cnt 