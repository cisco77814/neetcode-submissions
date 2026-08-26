class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            is_duplicate = nums[i]

            if is_duplicate in seen:
                return True
            
            seen.add(is_duplicate)
        return False