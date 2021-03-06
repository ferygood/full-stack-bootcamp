def maxProduct(nums):
    # 從大到小排序
    sort_nums = sorted(nums, reverse=True)
    # 取最大的兩位相乘
    product = sort_nums[0]*sort_nums[1]
    return product

print(maxProduct([5,20,2,6])) #120
print(maxProduct([10,-20,0,3])) #30

