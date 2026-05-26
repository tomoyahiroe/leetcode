class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3: return False
        ans = False
        n = len(nums)
        for i in range(n):
            vi = nums[i]
            for j in range(n-i-1):
                vj = nums[j+i+1]
                if vi>=vj:
                    continue
                for k in range(n-j-i-2):
                    vk = nums[k+j+i+2]
                    if vj>=vk:
                        continue
                    ans = True
                    break
                if ans == True: break
            if ans == True: break
        return ans