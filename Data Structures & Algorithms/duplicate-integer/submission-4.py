class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for i in range(len(nums)):
            duplicate = nums[i]

            if duplicate in seen:
                return True
            
            else:
                seen.add(duplicate)
        return False