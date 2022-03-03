# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        t = 1
        for i in range(ord('a'), ord('z')+1):
            t *= sentence.count(chr(i))
        return t > 0

        
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = "".join(set(sentence))
        return len(s) == 26

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        characters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        return len(set(sentence)) == len(characters)

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        characters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for i in sentence:
            if len(set(sentence)) == len(characters):
                return True
            else:
                return False