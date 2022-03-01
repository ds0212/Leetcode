# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.


# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false

# Success
# Details
# Runtime: 32 ms, faster than 80.76% of Python3 online submissions for Rotate String.
# Memory Usage: 13.9 MB, less than 87.62% of Python3 online submissions for Rotate String.


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            # print(s[i:(len(s))] + s[:i])
            if (s[i : (len(s))] + s[:i]) == goal:
                return True
        else:
            return False
