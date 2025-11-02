def missingElements():        
    result = []
    nums.sort()
    numsSet = set(nums)
    for num in range(nums[0], nums[len(nums)-1]):
        if num not in numsSet:
            result.append(num)

    return result

nums =[1,2,4,5]