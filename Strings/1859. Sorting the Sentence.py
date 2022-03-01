# Example 1:

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
# Example 2:

# Input: s = "Myself2 Me1 I4 and3"
# Output: "Me Myself and I"
# Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.


class Solution:
    def sortSentence(self, s: str) -> str:
        s1 = []
        s3 = []
        s2 = []
        for i in s.split():
            s1.append(i[: len(i) - 1])
            s2.append(int(i[-1]) - 1)
        for i in range(len(s1)):
            index_pos = s2.index(i)
            s3.append(s1[index_pos])
        return " ".join(s3)
