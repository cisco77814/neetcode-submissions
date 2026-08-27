class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {}

        for i in range(len(nums)):
            looking_for = target - nums[i]

            if looking_for in dictionary:
                return [dictionary[looking_for], i]

            else: 
                dictionary[nums[i]] = i

        return []
        