# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in nums:
            new_list.append(i**2)
            new_list.sort()
        return new_list


# OR FASTER
# Runtime: 255 ms, faster than 69.69% of Python3 online submissions for Squares of a Sorted Array.
# Memory Usage: 16.3 MB, less than 40.02% of Python3 online submissions for Squares of a Sorted Array.


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = map(lambda x: x**2, nums)
        a = list(a)
        a.sort()
        return a


# OR
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a = map(lambda x: x**2, nums)

        return sorted(a)


# OR
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([i * i for i in nums])
