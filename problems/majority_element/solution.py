class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me = -1   # me = Majority Element
        count = 0      # count = Count of Majority Element
        
        for i in range(len(nums)):
            if nums[i] == me:
                count += 1
            elif count > 0 and nums[i] != me:
                count -= 1
            
            if count == 0:
                me = nums[i]
                count = 1
        
        print(me)
        if nums.count(me) >= len(nums) // 2:
            return me
        return -1