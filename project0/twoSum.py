def twoSum(nums, target):
    for i in range(len(nums)):
        for x in range(i,len(nums)):
            if(nums[i]+nums[x] == target):
                return i,x


