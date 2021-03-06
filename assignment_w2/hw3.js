function maxProduct(nums){
    var sort_nums = nums.sort(function(a,b){
        return b-a; // b-a > 0 反向排序
    });
    product = sort_nums[0] * sort_nums[1];
    return product;
}

console.log(maxProduct([5,20,2,6])); //120
console.log(maxProduct([10,-20,0,3])); //30