class Solution:
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

    
    def strStr_builtin(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        return haystack.find(needle)