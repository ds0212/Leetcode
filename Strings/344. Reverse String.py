# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        return s.reverse()


# OR
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s



# OR
# Runtime: 204 ms, faster than 80.65% of Python3 online submissions for Reverse String.
# Memory Usage: 18.6 MB, less than 33.99% of Python3 online submissions for Reverse String.
# Next challenges:

 class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """ 
        s2 = []
        for i in range(len(s)-1, -1, -1):
            s2.append(s[i])
        s[:] = s2
        return s
    