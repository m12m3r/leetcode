from typing import List

class Solution:
    def containsDuplicate1(self, nums: List[int]) -> bool:
        map = {}
        for n in nums:
            if n in map:
                return True
            map[n] = 1

        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
    def containsDuplicate3(self, nums: List[int]) -> bool:
        bucket = set()
        for n in nums:
            if n in bucket:
                return True
            bucket.add(n)
        return False