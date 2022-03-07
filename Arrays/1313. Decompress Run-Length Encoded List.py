# We are given a list nums of integers representing a list compressed with run-length encoding.

# Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

# Return the decompressed list.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [2,4,4,4]
# Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
# The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
# At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
# Example 2:

# Input: nums = [1,1,2,3]
# Output: [1,3,3]

class Solution:
     def decompressRLElist(self, nums: List[int]) -> List[int]:

          compressed_list = []

           for i in range(0, len(nums), 2):

                for j in range(nums[i]):
                    compressed_list.append(nums[i+1])

            return compressed_list


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        compressed_list = []

        for i in range(0, len(nums),2):
            compressed_list.extend([nums[i+1]]*nums[i])
        
        return compressed_list


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
            result = []
            i = 0
            j = 1
            while j < len(nums):
                freq = nums[i]
                val = nums[j]
                temp_list = [val] * freq
                result += temp_list
                i += 2
                j += 2
            return result