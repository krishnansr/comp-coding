class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since the array is sorted (unlike two sum) we can leverage that
        # and start at the ends of the arrays and iteratively narrow down on the indices
        l, r = 0, len(numbers) - 1
        while l < r:
            add = numbers[l] + numbers[r]
            if add == target:
                break  # sine q guaranteed exactly one solution
            elif add < target:
                l += 1
            else:
                r -= 1
        
        return [l + 1, r + 1]