def maxZeros(nums):
    zero_len = []
    nums.append(1) #在最後加一個 1 讓最後如果是0的話可以被計算
    count = 0
    for n in range(len(nums)):
        if nums[n] == 0:
            count = count + 1
        else:
            zero_len.append(count)
            count = 0

    return max(zero_len)

print(maxZeros([0,1,0,0])) #2
print(maxZeros([1,0,0,0,0,1,0,1,0,0])) #4
print(maxZeros([1,1,1,1,1])) #0