# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:

# Input: haystack = "", needle = ""
# Output: 0

# Runtime: 28 ms, faster than 97.38% of Python3 online submissions for Implement strStr().
# Memory Usage: 14.1 MB, less than 83.89% of Python3 online submissions for Implement strStr().
# Next challenges:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        if needle in haystack:
            return haystack.index(needle)

        else:
            return -1
