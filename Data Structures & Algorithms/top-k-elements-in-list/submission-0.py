class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count_nums = {}

        for i in range(len(nums)):
            have = nums[i]

            if have in count_nums:
                count_nums[have] += 1
            
            else:
                count_nums[have] = 1
            
        sorted_nums = sorted(count_nums, key=count_nums.get, reverse=True)
        return sorted_nums[:k]