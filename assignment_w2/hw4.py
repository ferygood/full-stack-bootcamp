def twoSum(nums, target):
    # 先將 target 拆成一半，減少時間
    # 舉例來說總和為 9 ，找 2 就和找 7 的意思一樣
    reduced = 0
    if target/2 == 0:
        reduced = int(target/2)
    else:
        reduced = int((target+1)/2)
    pool = list(range(reduced))

    idx = []
    for n in pool:
        if n in nums:
            idx1 = nums.index(n)
            idx2 = nums.index(target-n)
            idx.append(idx1)
            idx.append(idx2)
    return idx

result = twoSum([2,11,7,15], 9)
print(result) #[0,2]