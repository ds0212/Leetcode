# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.

 

# Example 1:

# Input: words = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".
# Example 2:

# Input: words = ["a"]
# Output: 1
 


#  Runtime: 34 ms, faster than 89.68% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.9 MB, less than 87.89% of Python3 online submissions for Unique Morse Code Words.

## WHY? T.C in the code is n^4

 class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
          
        s1 = []
        s2 = set()
        for i in words:
            li = []
            for j in i:
                li.append(ord(j) - 96)
            s1.append(li)
        
        for ele in s1:
            temp_str = ""
            for sub in ele:
                temp_str += (morse[sub-1])
                
            s2.add(temp_str)
        return len(s2)


### DECENT
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        abc = 'abcdefghijklmnopqrstuvwxyz'
        dic =  dict(zip(abc,morse))
        words_list = []

        for word in words:
            word_result = ''
            for item in word:
                word_result += dic[item]

            words_list.append(word_result)
            word_result = ''
        return len(set(words_list))
