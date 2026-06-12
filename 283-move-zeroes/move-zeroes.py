class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        zc = 0 # zero counter
        while i <= n-zc and i < n:
            if nums[i] == 0:
                zc += 1
                nums.append(0)
                nums.pop(i)
                continue
            i += 1
