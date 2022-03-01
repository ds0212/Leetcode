# Example 1:

# Input: s = "Hello"
# Output: "hello"
# Example 2:

# Input: s = "here"
# Output: "here"
# Example 3:

# Input: s = "LOVELY"
# Output: "lovely"


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()





class Solution:
    def toLowerCase(self, s: str) -> str:
        s1 = ''
        for i in s:
            if i.isupper():
                s1 += i.lower()
            else:
                s1 += i 
        s = s1
        del s1
        return s