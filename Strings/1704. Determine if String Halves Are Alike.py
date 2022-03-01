# Example 1:

# Input: s = "book"
# Output: true
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:

# Input: s = "textbook"
# Output: false
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        count1 = 0
        count2 = 0

        for j in range(len(s[:mid])):
            if s[:mid][j].lower() in "aeiou":
                count1 += 1

        for k in range(len(s[mid:])):
            if s[mid:][k].lower() in "aeiou":
                count2 += 1

        if count1 == count2:
            return True
        else:
            return False
