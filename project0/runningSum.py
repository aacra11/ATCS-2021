def runningSum(nums):
    sums = []
    for i in range(len(nums)):
        sum = 0
        while (i>=0):
            sum = sum + nums[i]
            i = i-1
        sums.append(sum)
    return sums

