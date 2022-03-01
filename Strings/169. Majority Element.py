# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        set1 = set(nums)
        dict1 = {}
        for i in set1:
            dict1[i] = nums.count(i)
        return max((dict1), key=dict1.get)
