from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset=set(nums)
        longest=0
        for item in myset:
            if item-1 not in myset:
                length=1
                while item+length in myset:
                    length+=1
                longest=max(length,longest)
        return longest
    
print (Solution.longestConsecutive(self="",nums=[100,4,200,1,3,2]))