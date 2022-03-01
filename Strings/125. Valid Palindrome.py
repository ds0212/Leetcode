# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_s = ""
        for i in s:
            if i in "!#@$%`^&_-*():=|,;[]{}+-<>?{}.'\"":
                continue
            else:
                updated_s += i.lower()
                updated_s = updated_s.replace(" ", "")
        if updated_s[:] == updated_s[::-1]:
            return True
        else:
            return False
