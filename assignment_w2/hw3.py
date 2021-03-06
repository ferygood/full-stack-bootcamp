def maxProduct(nums):
    product_list = []
    for n in range(len(nums)-1):
        for m in range(n+1,len(nums)):
            product = nums[n]*nums[m]
            product_list.append(product)
    return max(product_list)

print(maxProduct([5,20,2,6])) #120
print(maxProduct([10,-20,0,3])) #30
print(maxProduct([-10,-20,1,2])) #200