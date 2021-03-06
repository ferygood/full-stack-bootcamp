function maxProduct(nums){
    var product_list = [];
    for (n=0; n<nums.length-1; n++){
        for (m=n+1; m<nums.length; m++){
            var product = nums[n]*nums[m];
            product_list.push(product);
        }
    }
    return Math.max.apply(Math,product_list);
}

console.log(maxProduct([5,20,2,6])); //120
console.log(maxProduct([10,-20,0,3])); //30
console.log(maxProduct([-10,-20,1,2])); //200