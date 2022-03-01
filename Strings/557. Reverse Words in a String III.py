# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"


# Runtime: 32 ms, faster than 92.82% of Python3 online submissions for Reverse Words in a String III.
# Memory Usage: 14.7 MB, less than 52.69% of Python3 online submissions for Reverse Words in a String III.
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        s1 = s.split()
        for i in s1:
            stri = ""
            str1 = list(reversed(i))
            a = stri.join(str1)
            ans.append(a)
        return " ".join(ans)
