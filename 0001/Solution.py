from typing import List

class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in map:
                return [i, map[comp]]
            map[n] = i
