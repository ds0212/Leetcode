# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str((int(num1) + int(num2)))
