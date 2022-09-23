class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        suffix = prefix = 1

        for i in range(len(nums)):
            ans[i] = ans[i] * prefix
            ans[- i - 1] = ans[- i - 1] * suffix
            
            prefix = prefix * nums[i]
            suffix = suffix * nums[-i - 1]
        return ans
        
        
    def productExceptSelf_2pass(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        ans2 = [1] * len(nums)

        for i in range(len(nums) - 1):
            ans[i + 1] = ans[i]* nums[i]

        for i in range(len(nums) - 1):
            ans2[i + 1] = ans2[i] * nums[len(nums) - 1 - i]
        
        return [x*y for x, y in zip(ans, ans2[::-1])]
            
        
    # def productExceptSelf_np(self, nums: List[int]) -> List[int]:
    #     # MLE
    #     prod_array = np.vstack([np.full(len(nums), n) for n in nums])
    #     np.fill_diagonal(prod_array, 1)
    #     return np.prod(prod_array, axis=0).tolist()