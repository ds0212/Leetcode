# Example 1:

# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:

# Input: s = "Hello"
# Output: 1


class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())


## Excellent approach:
class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        inWord = False
        for c in s:
            if c != " ":
                if not inWord:
                    inWord = True
                    ans += 1
            else:
                inWord = False
        return ans
