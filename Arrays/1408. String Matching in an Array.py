# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
 


 class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        subString_list = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i  == j:
                    continue
                else:
                    if words[i] in words[j]:
                        subString_list.append(words[i])
                        break
        return subString_list


# OR
        return {w for word in words for w in words if w in word and w != word}