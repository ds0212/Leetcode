# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.


# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.capitalize():
            return True
        if word == word.upper():
            return True
        if word == word.lower():
            return True
        else:
            return False


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return ((word == word.capitalize()) or (word == word.upper()) or (word == word.lower()))
