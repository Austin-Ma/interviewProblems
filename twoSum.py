    def twoSum(self, nums, target):
        store_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in store_dict:
                return [store_dict[nums[i]], i]
            else:
                store_dict[diff]= i
            
