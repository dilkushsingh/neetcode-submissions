class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Approach 1: two loops O(n^2) O(1)
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True
        # return False


        # Approach 2: Frequency Map O(n) O(n)
        # freq_map = {}
        # for num in nums:
        #     if num in freq_map:
        #         freq_map[num] += 1
        #     else:
        #         freq_map[num] = 1
        
        # for num, count in freq_map.items():
        #     if count != 1:
        #         return True
        # return False


        # Approach 3: Hash Set O(n) O(n)
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False


        