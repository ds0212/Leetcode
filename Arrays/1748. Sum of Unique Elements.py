# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        sum_of_totals = []

        for i in nums:
            if nums.count(i) > 1:
                continue
            else:
                sum_of_totals.append(i)

        return sum(sum_of_totals)


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        return sum([i for i in nums if nums.count(i) < 2])
