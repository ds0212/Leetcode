# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len_word1 = len(word1)
         len_word2 = len(word2)
          stri = ""

           if len_word1 > len_word2:
                j = 0
                for i in range(len_word2):
                    if j > len_word2:
                        break
                    if i == j:
                        stri += word1[i] + word2[j]
                    j += 1
                    # print(stri)
                stri += word1[-(len_word1-len_word2):]
            # return stri

            elif len_word2 > len_word1:
                j = 0
                for i in range(len_word1):
                    if j > len_word1:
                        break
                    if i == j:
                        stri += word1[i] + word2[j]
                    j += 1
                    # print(stri)
                stri += word2[-(len_word2-len_word1):]

            elif len_word2 == len_word1:
                j = 0
                for i in range(len_word1):
                    if i == j:
                        stri += word1[i] + word2[j]
                    j += 1

            return stri
