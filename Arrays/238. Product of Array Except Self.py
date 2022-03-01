# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 



 # Time limit exceeded:



 class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            demo = []
            for j in range(len(nums)):
                if  i == j:
                    continue
                else:
                    demo.append(nums[j])
            a = self.product(demo)
            ans.append(a)
        return ans
    
    def product(self, nums):
    
        total = 1
        for i in nums:
            total *= i 
        return total          
            
    
    
