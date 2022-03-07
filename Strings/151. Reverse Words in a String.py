# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        temp_list = s.split()
        return " ".join(list(reversed(temp_list)))


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        return " ".join(list(reversed(s.split())))


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(list(reversed(s.strip().split())))


class Solution:
    def reverseWords(self, s: str) -> str:

        if s == '':
            return s
        ls = s.split()
        result = ""
        for i in range(len(ls)-1):
            result += ls[len(ls)-1-i]+" "
        result += ls[0]
        return result
