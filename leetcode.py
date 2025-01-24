class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            target_num = target - num
            if target_num in hashmap:
                return [hashmap[target_num], index]
            hashmap[num] = index

            
solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # [1, 2]
print(solution.twoSum([3, 3], 6))          # [0, 1]