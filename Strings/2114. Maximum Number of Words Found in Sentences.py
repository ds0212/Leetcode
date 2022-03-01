# Example 1:

# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6
# Explanation:
# - The first sentence, "alice and bob love leetcode", has 5 words in total.
# - The second sentence, "i think so too", has 4 words in total.
# - The third sentence, "this is great thanks very much", has 6 words in total.
# Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
# Example 2:

# Input: sentences = ["please wait", "continue to fight", "continue to win"]
# Output: 3
# Explanation: It is possible that multiple sentences contain the same number of words.
# In this example, the second and third sentences (underlined) have the same number of words.


# Constraints:

# 1 <= sentences.length <= 100
# 1 <= sentences[i].length <= 100
# sentences[i] consists only of lowercase English letters and ' ' only.
# sentences[i] does not have leading or trailing spaces.
# All the words in sentences[i] are separated by a single space.


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        li = []

        for i in sentences:
            li.append(len(i.split()))
        return max(li)


return max(list(map(lambda x: len(x.split()), sentences)))


return max([len(i.split())for i in sentences])



# Low TC
class Solution:
def mostWordsFound(self, sentences: List[str]) -> int:
    mx=0
    for i in range(len(sentences)):
        l=len(sentences[i].split())
        if l>mx:
            mx=l
    return mx
