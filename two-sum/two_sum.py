def twoSum():
    nums = [1, 4, 6, 4, 2, 5]
    target = 7

    for i in range(len(nums)):
        remaining = target - nums[i]
        for j in range(len(nums)):
            if i != j and nums[j] == remaining:
                print(f"The indexes are {i} and {j} which contain {nums[i]} and {nums[j]} = {target}")
                return  

twoSum()
