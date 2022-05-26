from typing import *
from functools import lru_cache
from itertools import repeat
from math import *
from collections import OrderedDict

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range(len(nums)):
            if not nums[j] & 1:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] & 1 == 0:
                i += 2
            while j < len(nums) and nums[j] & 1 == 1:
                j += 2
            else:
                if i < len(nums) and j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 2
                    j += 2
        return nums

    def sortArrayByParityIII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] & 1 == 0:
                i += 2
            elif nums[j] & 1 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]

        return nums

    def largestInteger(self, num: int) -> int:
        parity = []
        counter_ls = [[], []]

        while num > 0:
            _digit = num % 10
            counter_ls[_digit & 1].append(_digit)
            parity.insert(0, _digit & 1)
            num //= 10

        counter_ls[0].sort()
        counter_ls[1].sort()

        res = 0
        for par in parity:
            res = res * 10 + counter_ls[par].pop()

        return res

    def findShortestSubArray(self, nums: List[int]) -> int:
        first_seen, counter = {}, {}
        degree, res = 0, 0

        for i, n in enumerate(nums):
            first_seen.setdefault(n, i)
            counter[n] = counter.get(n, 0) + 1

            if counter[n] > degree:
                degree = counter[n]
                res = i - first_seen[n] + 1
            elif counter[n] == degree:
                res = min(res, i - first_seen[n] + 1)

        return res

    def kthDistinct(self, arr: List[str], k: int) -> str:
        dist_map = OrderedDict()

        for word in arr:
            if word in dist_map:
                dist_map[word] = -1
            else:
                dist_map[word] = 1

        i = 0
        for k, v in dist_map.items():
            if v == 1:
                i += 1
                if i == k:
                    return k

        return ''

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # compute LPS table for KMP algorithm
        lps = [0] * len(needle)
        prev_lps, i = 0, 1
        while i < len(needle):
            if needle[prev_lps] == needle[i]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]

        # Haystack traversal for KMP algorithm
        i = 0  # haystack pointer
        j = 0  # needle pointer
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = lps[j - 1]

            if j == len(needle):
                return i - j

        return -1

    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        arr = [False] * (right - left + 1)
        for l, r in ranges:
            l -= left
            r -= left

            if r >= 0 and l < len(arr):
                l = max(l, 0)
                r = min(r, len(arr) - 1)
                arr[l: r + 1] = repeat(True, r + 1 - l)

        return sum(arr) == len(arr)

    def numDifferentIntegers(self, word: str) -> int:
        int_set = set()
        st = -1
        for i in range(len(word)):
            if word[i].isnumeric():
                if st == -1:
                    st = i
            else:
                if st != -1:
                    int_set.add(int(word[st:i]))
                st = -1

        if st != -1:
            int_set.add(int(word[st:]))

        return len(int_set)


    def moveZeroes(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums

    def checkIfExist(self, arr: List[int]) -> bool:
        pair_arr = [0] * 2001
        for i in arr:
            _match = (i >= 0) - (i < 0)
            if pair_arr[2 * i] == _match or (not i & 1 and pair_arr[i // 2] == _match):
                return True
            pair_arr[i] = _match
        return False

    def checkIfExist_old(self, arr: List[int]) -> bool:
        pair_arr = [0] * 2001
        for i in arr:
            if i > 0:
                if pair_arr[2 * i] == 1:
                    return True
                if not i & 1:
                    if pair_arr[i // 2] == 1:
                        return True
                pair_arr[i] = 1
            elif i < 0:
                i = abs(i)
                if pair_arr[2 * i] == 2:
                    return True
                if not i & 1:
                    if pair_arr[i // 2] == 2:
                        return True
                pair_arr[i] = 2
            else:
                pair_arr[0] += 1
                if pair_arr[0] > 1:
                    return True
        return False

    def validPalindrome(self, s: str, max_deletes: int=1) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                if max_deletes:
                    return self.validPalindrome(s[i: j], 0) or self.validPalindrome(s[i + 1: j + 1], 0)
                else:
                    return False
            i += 1
            j -= 1

        return True


    def binaryGap(self, n: int) -> int:
        if n & (n - 1) == 0:
            return 0

        max_dist, prev = 0, -1
        for i, b in enumerate(bin(n)[3:]):
            if b == '1':
                max_dist = max(max_dist, i - prev)
                prev = i
        return max_dist


    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False

        return True

    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        digits = ''
        len_a = len(a)
        len_b = len(b)

        for i in range(1, max(len_a, len_b) + 1):
            a_i = 0 if i > len_a else int(a[-i])
            b_i = 0 if i > len_b else int(b[-i])

            _sum = a_i + b_i + carry
            digits, carry = str(_sum % 2) + digits, _sum // 2

        return '1' + digits if carry else digits

    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            _sum = digits[i] + carry
            digits[i], carry = _sum % 10, _sum // 10

        return [1] + digits if carry else digits

    @lru_cache(maxsize=50)
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def strStr_builtin(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1

    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l, r, i = 0, len(nums) - 1, len(nums) - 1
        while l <= r:
            left_val, right_val = abs(nums[l]), abs(nums[r])
            if left_val > right_val:
                res[i] = left_val ** 2
                l += 1
            else:
                res[i] = right_val ** 2
                r -= 1
            i -= 1  # to fill next biggest value
        return res

    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        del_i, del_j = 0, 0
        while i > -1 or j > -1:
            if i > -1  and (s[i] == '#' or del_i):
                del_i += 1 if s[i] == '#' else -1
                i -= 1
                continue

            if j > -1 and (t[j] == '#' or del_j):
                del_j += 1 if t[j] == '#' else -1
                j -= 1
                continue

            if s[i] != t[j]:
                return False

            i -= 1
            j -= 1
        return i == j

    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        return [original[n * x : n * x + n] for x in range(m)]


if __name__ == '__main__':
    s = Solution()
    # print(s.strStr('hello', 'll'))
    # print(s.strStr('abc', 'abcd'))
    # print(s.strStr('abc', 'a'))
    # print(s.strStr('mississippi', 'issip'))
    # print(s.countBits(2))
    # print(s.hammingWeight('00000000000000000000000000000000'))
    # print(s.hammingWeight('00000000000000000000000000000001'))
    # print(s.hammingWeight('00000000000000000000000000000010'))
    # print(s.hammingWeight('00000000000000000000000000001011'))
    # print(s.pivotIndex([1,7,3,6,5,6]))
    # print(s.plusOne([1,2,3]))
    # print(s.addBinary('11', '1'))
    # print(s.isPalindrome("A man, a plan, a canal: Panama"))
    # print(s.binaryGap(22))
    # print(s.binaryGap(6))
    # print(s.binaryGap(7))
    # print(s.validPalindrome("aba"))
    # print(s.validPalindrome("abca"))
    # print(s.validPalindrome("ebcbbececabbacecbbcbe"))
    # print(s.validPalindrome("abc"))
    # print(s.checkIfExist([10,2,5,3]))
    # print(s.moveZeroes([1,3,12,0]))
    # print(s.numDifferentIntegers('a123bc34d8ef34'))
    # print(s.isCovered(ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5))
    # print(s.isCovered(ranges = [[5,10],[10,20]], left = 21, right = 21))
    # print(s.isCovered(ranges = [[5,10],[10,20]], left = 2, right = 20))
    # print(s.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))
    # print(s.findShortestSubArray(nums = [1,2,2,3,1]))
    # print(s.largestInteger(1234))
    # print(s.sortArrayByParityII([2,3]))
    # print(s.sortArrayByParity([3, 1, 2, 4]))
    # print(s.search([-1,0,3,5,9,12], 9))
    # print(s.sortedSquares([-7,-3,2,3,11]))
    # print(s.backspaceCompare(s = "ab#c", t = "ad#c"))
    print(s.construct2DArray(original=[1, 2, 3, 4], m=2, n=2))
    print(s.construct2DArray(original=[1, 2, 3], m=1, n=3))
    print(s.construct2DArray(original=[1, 2, 3, 4, 5, 6], m=3, n=2))
    print(s.construct2DArray(original = [1,1,1,1], m = 4, n = 1))
    print(s.construct2DArray(original = [1,1,1,1], m = 1, n = 4))

