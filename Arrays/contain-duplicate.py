from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return True
        return False
    
print(Solution.containsDuplicate(self="",nums=[1,1,1,3,3,4,3,2,4,2]))