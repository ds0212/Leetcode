# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Time complexity O(n^2)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        li = []
        for i in range(m):
            li.append(nums1[i])
        for j in range(n):
            li.append(nums2[j])
        li.sort()
        nums1[:] = li

# Time complexity O(n) 
class Solution: 
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        li = []
        li = nums1[:m] + nums2[:n]
        li.sort()
        nums1[:] = li

        #
        # nums1[:] = nums1[:m] + nums2[:n]
        # nums1.sort()
       

# print(Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
