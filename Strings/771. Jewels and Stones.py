# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for i in stones:
            if i in jewels:
                count += 1

        return count


return len([count for count in stones if count in jewels])
